import pytest
from src.aeroplanes_information import Aeroplane


@pytest.mark.parametrize("aeroplane, ID, country, velocity, altitude",
                         [(Aeroplane("123456","Japan",289.68,10668), "123456", "Japan", 289.68, 10668),
                          (Aeroplane("789621","Canada",450,5000), "789621", "Canada", 450, 5000),
                          (Aeroplane("451292","Canada",100,None), "451292", "Canada", 100, 0)])
def test_init(aeroplane, ID, country, velocity, altitude):
    """тестирование создания класса самолет и проверка добавления нового товара в список и
    проверка на тип добавляемого объекта"""
    assert aeroplane.ID == ID
    assert aeroplane.country == country
    assert aeroplane.velocity == velocity
    assert aeroplane.altitude == altitude


@pytest.mark.parametrize("aeroplane, second_value",
                         [(Aeroplane("123456","Japan",289.68,10668),
                          Aeroplane("789621","Canada",450,5000)),
                          (Aeroplane("451292","Canada",100,None), 500),
                          (Aeroplane("451292","Canada",None,None), 100)])
def test_lt(aeroplane, second_value):
    """тестирование сравнение двух самолетов по высоте на меньше"""
    assert aeroplane < second_value

def test_lt_error(aeroplane_type):
    """тестирование сравнение двух самолетов по высоте на меньше с ошибкой"""
    with pytest.raises(TypeError) as exc_info:
         aeroplane_type < '100'

    assert str(exc_info.value) == "Операнд справа должен иметь тип float или int или Aeroplane"


@pytest.mark.parametrize("aeroplane, second_value",
                         [(Aeroplane("123456","Japan",289.68,10668),
                          Aeroplane("789621","Canada",None,5000)),
                          (Aeroplane("451292","Canada",450,None), 120),
                          (Aeroplane("451292","Canada",100,None), 0)])
def test_gt(aeroplane, second_value):
    """тестирование сравнение двух самолетов по высоте на меньше"""
    assert aeroplane > second_value

def test_gt_error(aeroplane_type):
    """тестирование сравнение двух самолетов по высоте на меньше с ошибкой"""
    with pytest.raises(TypeError) as exc_info:
         aeroplane_type > '100'

    assert str(exc_info.value) == "Операнд справа должен иметь тип float или int или Aeroplane"


@pytest.mark.parametrize("list_to_sort, list_sort",
                         [([{"ID": "c07d0b",
                            "country": "Canada",
                            "velocity": 45.51,
                            "altitude": 1219.2
                        },
                        {
                            "ID": "c047d8",
                            "country": "Canada",
                            "velocity": 30.77,
                            "altitude": 259.08
                        },
                        {
                            "ID": "a4b234",
                            "country": "United States",
                            "velocity": 60.05,
                            "altitude": 335.28
                        }],
                           [{"ID": "c07d0b",
                             "country": "Canada",
                             "velocity": 45.51,
                             "altitude": 1219.2
                             },
{
                                "ID": "a4b234",
                                "country": "United States",
                                "velocity": 60.05,
                                "altitude": 335.28
                            },
                            {
                                "ID": "c047d8",
                                "country": "Canada",
                                "velocity": 30.77,
                                "altitude": 259.08
                            }
                            ]
                           )]
                          )
def test_sort_aeroplanes(list_to_sort, list_sort):
    assert Aeroplane.sort_aeroplanes(list_to_sort) == list_sort
