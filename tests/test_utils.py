from unittest.mock import mock_open, patch

from src.utils import *


def test_get_operation(operations_mocked_data):
    mocked_json_data = json.dumps(operations_mocked_data)
    m = mock_open(read_data=mocked_json_data)
    with patch("builtins.open", m):
        result = get_operations()
    assert result == operations_mocked_data


def test_remove_empty_items(operations_mocked_data, remove_mocked_data):
    with patch('src.utils.get_operations', return_value=operations_mocked_data):
        result = remove_empty_items()
    assert result == remove_mocked_data


def test_sort_key(dict_test):
    assert sort_key(dict_test) == "2019-08-26T10:50:58.294041"


def test_sort_data(remove_mocked_data, mocked_data_sort):
    with patch("src.utils.remove_empty_items", return_value=remove_mocked_data):
        result = sort_data()
    assert result == mocked_data_sort


def test_get_result_data(mocked_data_sort, mocked_result_data):
    with patch("src.utils.remove_empty_items", return_value=mocked_data_sort):
        result = get_result_data()
    assert result == mocked_result_data

