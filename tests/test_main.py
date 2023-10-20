from unittest.mock import patch

from src.main import *


def test_data_masking(mocked_data_masked_from, mocked_data_masked_to):
    assert data_masking("Visa Classic 2842878893689012", "from") == mocked_data_masked_from
    assert data_masking("Счет 35158586384610753655", "to") == mocked_data_masked_to


def test_format_date():
    assert format_date({"date": "2019-08-26T10:50:58.294041"}) == "26.08.2019"


# На второй вариант возврата с from я так и не смог реализовать тест
def test_format_result(mocked_data_to, mocked_result_data_to):
    with patch("src.main.data_masking", return_value="Счет 3515 **** **** 3655"):
        result = format_result(mocked_data_to, "26.08.2019")
        assert result.strip() == mocked_result_data_to.strip()


def test_main(mocked_data_result, mocked_result_data_to):
    with patch("src.main.get_result_data", return_value=mocked_data_result):
        with patch("src.main.format_date", return_value="26.08.2019"):
            with patch("src.main.format_result", return_value=mocked_result_data_to):
                results = main()
                assert results == [mocked_result_data_to] * 5
