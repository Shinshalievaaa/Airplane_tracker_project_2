import pytest
from src.aeroplanes_information import Aeroplane


@pytest.fixture
def aeroplane_type():
    return Aeroplane("123456","Japan",289.68,10668)


@pytest.fixture
def aeroplane_type2():
    return Aeroplane("789621","Canada",450,5000)


@pytest.fixture
def aeroplane_type3():
    return Aeroplane("451292","Canada",100,None)


@pytest.fixture
def mock_value_geo_coordinates():
    return {'lamin': "41.6765597",
            'lamax': "83.3362128",
            'lomin': "-141.0027500",
            'lomax':  "-52.3237664",
            }


@pytest.fixture
def mock_value():
    return {
    "time": 1766142246,
    "states": [
                [
                    "4b1812",
                    "SWR438A ",
                    "Switzerland",
                    1766166618,
                    1766166618,
                    -0.0168,
                    51.0888,
                    4267.2,
                    False,
                    189.7,
                    129.39,
                    14.63,
                    None,
                    4282.44,
                    "2061",
                    False,
                    0
                ]
            ]
            }


@pytest.fixture
def json_data():
    return [
    {
        "ID": "a35592",
        "country": "United States",
        "velocity": 0,
        "altitude": 0
    },
    {
        "ID": "abad94",
        "country": "United States",
        "velocity": 70.91,
        "altitude": -76.2
    },
    {
        "ID": "a5823e",
        "country": "United States",
        "velocity": 283.67,
        "altitude": 10066.02
    },
    {
        "ID": "a1bfb2",
        "country": "United States",
        "velocity": 289.8,
        "altitude": 10668
    },
    {
        "ID": "a16ff1",
        "country": "United States",
        "velocity": 275.3,
        "altitude": 10668
    },
    {
        "ID": "ab048d",
        "country": "United States",
        "velocity": 279.99,
        "altitude": 11887.2
    }]


@pytest.fixture
def ID_list():
    return ["a35592","abad94","a5823e","a1bfb2","a16ff1","ab048d"]