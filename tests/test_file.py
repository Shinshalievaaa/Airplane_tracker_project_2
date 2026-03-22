import pytest
import json
from src.file import JSONSaver


@pytest.fixture
def json_saver_instance(tmp_path):
    file_path = 'data/data_json_test.json'
    saver = JSONSaver(file_path)
    return saver, file_path

@pytest.fixture
def sample_aeroplanes_data():
    return [
        ["ID001", "typeA", "USA", "icaoA", "regA", "callA", "onGnd", 1000, 150, 500, "squawkA", "altA", "latA", "lonA", "trackA", "spiA", "mlatA", "tisA"],
        ["ID002", "typeB", "Germany", "icaoB", "regB", "callB", "onGnd", 2000, 200, None, "squawkB", "altB", "latB", "lonB", "trackB", "spiB", "mlatB", "tisB"],
        ["ID003", "typeC", "USA", "icaoC", "regC", "callC", "onGnd", None, 250, 600, "squawkC", "altC", "latC", "lonC", "trackC", "spiC", "mlatC", "tisC"],
        ["ID004", "typeD", "France", "icaoD", "regD", "callD", "onGnd", 3000, 300, 700, "squawkD", "altD", "latD", "lonD", "trackD", "spiD", "mlatD", "tisD"],
    ]


def test_add_aeroplane(json_saver_instance, sample_aeroplanes_data):
    saver, file_path = json_saver_instance
    saver.add_aeroplane(sample_aeroplanes_data)

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    expected_data = [
        {"ID": "ID001", "country": "USA", "velocity": 500, "altitude": 1000},
        {"ID": "ID002", "country": "Germany", "velocity": 0, "altitude": 2000}, # velocity is None in sample_aeroplanes_data
        {"ID": "ID003", "country": "USA", "velocity": 600, "altitude": 0}, # altitude is None in sample_aeroplanes_data
        {"ID": "ID004", "country": "France", "velocity": 700, "altitude": 3000}
    ]
    assert data == expected_data


def test_get_info_filter_by_country(json_saver_instance):
    saver, file_path = json_saver_instance
    print(saver)
    print(file_path)
    Germany_aeroplanes = saver.get_info(['Germany'])
    expected_Germany = [
        {"ID": "ID002", "country": "Germany", "velocity": 0, "altitude": 2000}
    ]
    assert Germany_aeroplanes == expected_Germany

    non_existent_country = saver.get_info(countries_to_filter=["Israel"])
    assert non_existent_country == []

def test_get_info_file_not_found(json_saver_instance):
    file_path = 'data/data_json_test_123.json'
    saver = JSONSaver(file_path)
    info = saver.get_info(countries_to_filter=["USA"])
    assert info == []

def test_get_info_invalid_json(json_saver_instance):
    """тестирование получения данных из некорректного файла"""
    saver, file_path = json_saver_instance
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("{\n  \"ID\": \"124596\"\n  \"country\": \"Kazakhstan\"\n}")

    info = saver.get_info(countries_to_filter=["Kazakhstan"])
    assert info == []

