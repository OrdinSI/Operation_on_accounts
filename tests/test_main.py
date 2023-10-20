from unittest.mock import patch
from src.main import main


def test_main(mocked_result_data):
    with patch("src.main.main", return_value=mocked_result_data):
        result = main()
    assert result
