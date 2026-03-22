class Aeroplane:

    ID : str # уникальный идентификатор борта
    callsign : str # позывной рейса
    country : str # Страна регистрации
    time_position : int # время последнего обновления позиции
    last_contact : int # время последнего контакта
    longitude : float # долгота(°)
    latitude : float # широта(°)
    altitude : float # высота(м)
    on_ground : bool # находится ли самолёт на земле
    velocity : float # горизонтальная скорость(м / с)
    true_track : float # курс(градусы)
    vertical_rate : float # вертикальная скорость(м / с)
    sensors : str # ID сенсоров(null=неизвестно)
    geo_altitude : float # геометрическая высота(м)
    squawk :str # код ответчика(транспондера)
    spi : bool # специальный сигнал(emergency / priority)
    position_source : int # источник позиции

    def __init__(self, ID, country, velocity, altitude) -> None:
        self.ID = ID
        self.country = country
        if not isinstance(velocity, (float,int)):
            self.velocity = 0
        else:
            self.velocity = velocity
        if not isinstance(altitude, (float,int)):
            self.altitude = 0
        else:
            self.altitude = altitude


    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (float, int, Aeroplane)):
            raise TypeError("Операнд справа должен иметь тип float или int или Aeroplane")

        return other if isinstance(other, (float, int)) else other.velocity


    def __lt__(self, other) -> None:
        velocity_other = self.__verify_data(other)
        return self.velocity < velocity_other


    def __gt__(self, other) -> None:
        velocity_other = self.__verify_data(other)
        return self.velocity > velocity_other


    def __str__(self):
        return f'ID: {self.ID}, country: {self.country}, velocity = {self.velocity}, altitude = {self.altitude}'


    @staticmethod
    def cast_to_object_list(aeroplanes: dict) -> list:
        return aeroplanes['states']


    @staticmethod
    def get_aeroplanes_by_altitude(filtered_aeroplanes: list[dict], altitude_range: list) -> list[dict]:
        """Получение данных в диапазоне высот"""

        try:
            range_min = int(altitude_range[0])
        except ValueError:
            print("В диапазоне должны быть указаны только числа")
        try:
            range_max = int(altitude_range[1])
        except ValueError:
            print("В диапазоне должны быть указаны только числа")

        filtered_data = []

        for item in filtered_aeroplanes:

            if item.get('altitude') >= range_min and item.get('altitude') <= range_max:
                filtered_data.append(item)

        return filtered_data


    @staticmethod
    def sort_aeroplanes(ranged_aeroplanes: list[dict]) -> list[dict]:
        """Сортировка данных по высоте"""
        return sorted(ranged_aeroplanes, key=lambda x: x['altitude'], reverse=True)


    @staticmethod
    def get_top_aeroplanes(sorted_aeroplanes: list[dict], top_n) -> list:
        """Получение top_n самолетов"""
        top_n_aeroplanes = sorted_aeroplanes[0:top_n - 1]
        list_aeroplanes = []
        for aeroplane in top_n_aeroplanes:
             list_aeroplanes.append(Aeroplane(**aeroplane))

        return list_aeroplanes


    @staticmethod
    def print_aeroplanes(top_aeroplanes: list, top_n: int, altitude_range: str):
        """Печать списка самолетов"""
        print(f'Топ {top_n} самолетов с диапазоном {altitude_range}:')
        for item in top_aeroplanes:
            print(item)