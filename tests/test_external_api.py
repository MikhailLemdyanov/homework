import json
from unittest.mock import patch

import pytest

from src.external_api import currency_convert


@patch("requests.get")
def test_currency_convert(mock_get, transaction_for_conversion, result_of_conversion):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = json.loads(result_of_conversion)
    result = currency_convert(transaction_for_conversion)
    assert result == 531.307615


def test_currency_convert_with_rub(transactions_list):
    result = currency_convert(transactions_list[2])

    assert result == 43318.34


@patch("requests.get")
def test_currency_convert_invalid_result(mock_get, transaction_for_conversion, result_of_conversion_without_result):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = json.loads(result_of_conversion_without_result)

    with pytest.raises(ValueError) as exc_info:
        currency_convert(transaction_for_conversion)

        assert str(exc_info.value) == "Недостаточно данных для конвертации"


@patch("requests.get")
def test_currency_convert_with_key_error(mock_get, transaction_for_conversion_invalid):
    with pytest.raises(KeyError) as exc_info:
        currency_convert(transaction_for_conversion_invalid)

        assert str(exc_info.value) == "Не найдены необходимые данные для конвертации"
