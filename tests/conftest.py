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