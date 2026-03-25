from unittest.mock import patch
from src.api import AeroplanesAPI
from tests.conftest import mock_value_geo_coordinates


@patch('requests.get')
def test_get_geo_coordinates(mock_get, mock_value_geo_coordinates):
    aeroplanes_api = AeroplanesAPI()
    mock_get.return_value.json.return_value = {
        "place_id": 346277167,
        "boundingbox": [
            "41.6765597",
            "83.3362128",
            "-141.0027500",
            "-52.3237664"
        ]
    }

    assert aeroplanes_api.get_geo_coordinates('Canada') == mock_value_geo_coordinates
