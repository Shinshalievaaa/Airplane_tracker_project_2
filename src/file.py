import json
import os
from abc import ABC, abstractmethod

class Saver(ABC):
    """Абстрактный класс для сохранения данных, полученных по API"""

    @abstractmethod
    def add_aeroplane(self, aeroplanes:list, path: str) -> None:
        pass

    @abstractmethod
    def get_info(self, **params) -> list[dict]:
        pass

    @abstractmethod
    def delete_aeroplane(self, ID:str) -> None:
        pass


class JSONSaver(Saver):
    """Клас для сохранения данных в JSON"""
    def __init__(self, path: str) -> None:
        self.path = path

    def add_aeroplane(self, aeroplanes: list) -> None:
        json_list = []

        for state in aeroplanes:
            json_new = {}
            json_new["ID"] = state[0]
            json_new["country"] = state[2]
            if state[9] is None:
                json_new["velocity"] = 0
            else:
                json_new["velocity"] = state[9]
            if state[7] is None:
                json_new["altitude"] = 0
            else:
                json_new["altitude"] = state[7]
            json_list.append(json_new)

        # Запись в JSON файл
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(json_list, file, ensure_ascii=False, indent=4)

    def get_info(self, countries_to_filter: list) -> list[dict]:

        filtered_data = []

        try:
            # Read the JSON file
            with open(self.path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Iterate through the data and filter by country
            for item in data:
                if countries_to_filter == []:
                    filtered_data.append(item)
                if item.get('country') in countries_to_filter:
                    filtered_data.append(item)

        except FileNotFoundError:
            print(f"Error: The file {self.path} was not found.")
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from the file {self.path}.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return filtered_data


    def delete_aeroplane(self, ID_list: list) -> None:

        try:
            # Read the JSON file into a list of dictionaries
            with open(self.path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Filter out entries with IDs that are present in the ID_list
            updated_data = [item for item in data if item.get('ID') not in ID_list]

            # Write the updated list of dictionaries back to the JSON file
            with open(self.path, 'w', encoding='utf-8') as file:
                json.dump(updated_data, file, ensure_ascii=False, indent=4)

            print(f"Successfully removed entries with IDs {ID_list} from {self.path}.")
            print("Updated data saved to file. Displaying updated data:")

        except FileNotFoundError:
            print(f"Error: The file {self.path} was not found.")
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from the file {self.path}. Please ensure it's a valid JSON file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")