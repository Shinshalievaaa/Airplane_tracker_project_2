from src.api import AeroplanesAPI
from src.aeroplanes_information import Aeroplane
from src.file import JSONSaver


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    country = input("Введите название страны: ")

    api = AeroplanesAPI()
    api.get_aeroplanes(country)
    aeroplanes = api.aeroplanes
    aeroplanes = Aeroplane.cast_to_object_list(aeroplanes)

    json_saver = JSONSaver("data/data_json.json")
    json_saver.add_aeroplane(aeroplanes)

    filter_words = input("Введите названия стран через запятую для фильтрации по стране регистрации: ").split(",")
    filtered_aeroplanes = json_saver.get_info(filter_words)

    top_n = int(input("Введите количество самолетов для вывода в топ N: "))
    altitude_range = input("Введите диапазон высот полета через тире: ") # Пример: 100000 - 150000

    ranged_aeroplanes = Aeroplane.get_aeroplanes_by_altitude(filtered_aeroplanes, altitude_range.split("-"))

    sorted_aeroplanes = Aeroplane.sort_aeroplanes(ranged_aeroplanes)

    top_aeroplanes = Aeroplane.get_top_aeroplanes(sorted_aeroplanes, top_n)
    Aeroplane.print_aeroplanes(top_aeroplanes, top_n, altitude_range)


if __name__ == "__main__":
    user_interaction()