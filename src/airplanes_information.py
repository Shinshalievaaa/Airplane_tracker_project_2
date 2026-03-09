class Airplane():

    ID_airplane : str # уникальный идентификатор борта
    Callsign : str # позывной рейса
    Country : str # Страна регистрации
    time_position : int # время последнего обновления позиции
    last_contact : int # время последнего контакта
    longitude : float # долгота(°)
    latitude : float # широта(°)
    baro_altitude : float # барометрическая высота(м)
    on_ground : bool # находится ли самолёт на земле
    velocity : float # горизонтальная скорость(м / с)
    true_track : float # курс(градусы)
    vertical_rate : float # вертикальная скорость(м / с)
    sensors : str # ID сенсоров(null=неизвестно)
    geo_altitude : float # геометрическая высота(м)
    squawk :str # код ответчика(транспондера)
    spi : bool # специальный сигнал(emergency / priority)
    position_source : int # источник позиции

    def __init__(self):
        pass