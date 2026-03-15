from src.api import AeroplanesAPI
from src.aeroplanes_information import Aeroplane
from src.file import JSONSaver


# Создание экземпляра класса для работы с API сайтов с самолетами
# api = AeroplanesAPI()

# Получение информации о самолетах с opensky-network.org
# api.get_aeroplanes('Canada')
# aeroplanes = api.aeroplanes

# Преобразование набора данных в список объектов
# print("--------------------------------")
# print(type(aeroplanes))
# aeroplanes = Aeroplane.cast_to_object_list(aeroplanes)

# print(aeroplanes)

# # Пример работы контструктора класса с одним самолетом
# aeroplane = Aeroplane("UAL1621", "United States", 268.79, 10203.18)
#
# # Сохранение информации в файл
# json_saver = JSONSaver("data/data_json.json")
# json_saver.add_aeroplane(aeroplanes)
# json_saver.delete_aeroplane(vacancy)

# Функция для взаимодействия с пользователем
def user_interaction():
    country = input("Введите название страны: ")
    api = AeroplanesAPI()
    api.get_aeroplanes(country)
    aeroplanes = api.aeroplanes
    aeroplanes = Aeroplane.cast_to_object_list(aeroplanes)
    json_saver = JSONSaver("data/data_json.json")
    json_saver.add_aeroplane(aeroplanes)
    # top_n = int(input("Введите количество самолетов для вывода в топ N: "))
    filter_words = input("Введите названия стран через запятую для фильтрации по стране регистрации: ").split(",")
    print(filter_words)
    # altitude_range = input("Введите диапазон высот полета: ") # Пример: 100000 - 150000

    # json_saver = JSONSaver()
    filtered_aeroplanes = json_saver.get_info(filter_words)

    print(filtered_aeroplanes)

    json_saver.delete_aeroplane(["ade18c", "a0f57e", "a808d7"])

    filtered_aeroplanes = json_saver.get_info(["United States"])
    print(filtered_aeroplanes)
    #
    # ranged_aeroplanes = get_aeroplanes_by_altitude(aeroplanes, altitude_range)
    #
    # sorted_aeroplanes = sort_aeroplanes(ranged_aeroplanes)
    # top_aeroplanes = get_top_aeroplanes(sorted_aeroplanes, top_n)
    # print_aeroplanes(top_aeroplanes)


if __name__ == "__main__":
    user_interaction()