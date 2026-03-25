from abc import ABC, abstractmethod

from requests import get


class API(ABC):

    @abstractmethod
    def get_aeroplanes(self, country: str):
        pass


class AeroplanesAPI(API):

    def __init__(self) -> None:
        self.openstreetmap_url = "https://nominatim.openstreetmap.org/search"
        self.opensky_url = "https://opensky-network.org/api/states/all?"
        self.aeroplanes = None

    def get_geo_coordinates(self, country: str) -> (dict, None):
        # Headers с user-agent - обязательный параметр при запросе к nominatim.openstreetmap.
        # Вы можете использовать любое название вместо test-app/1.0, например просто test-app.
        headers_nominatim = {
            "User-Agent": "test-app/1.0",
        }

        # Указываем параметры: в каком формате возвращать данные и максимальную длину списка стран в ответе.
        params_nominatim = {
            "country": country,
            "format": "json",
            "limit": 1,
        }

        response = get(
            url=self.openstreetmap_url,
            params=params_nominatim,
            headers=headers_nominatim,
            timeout=3
        )

        if response.status_code == 200:
            data = response.json()

            # Пример ответа от nominatim.openstreetmap можно посмотреть в задании курсовой.
            geo_coordinates = data[0].get("boundingbox")

            # Параметры для фильтрации самолетов по их географическим координатам.
            params = {
                "lamin": geo_coordinates[0],
                "lamax": geo_coordinates[1],
                "lomin": geo_coordinates[2],
                "lomax": geo_coordinates[3],
            }
            return params

        else:
            return None

    def get_aeroplanes(self, country: str) -> None:

        params = self.get_geo_coordinates(country)

        if params is None:
            self.aeroplanes = None
        else:
            response = get(url=self.opensky_url, params=params, timeout=3)

            if response.status_code == 200:
                # Пример ответа от opensky-network можно посмотреть в задании курсовой.
                self.aeroplanes = response.json()
            else:
                self.aeroplanes = None
