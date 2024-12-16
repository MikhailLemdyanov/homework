from unittest.mock import mock_open, patch

from src.utils import get_transactions_data


@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_get_transactions_data_correct_file(mock_file):
    transactions = get_transactions_data("data/operations.json")

    assert transactions == [{"amount": 100, "currency": "USD"}]
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_get_transactions_data_empty_file(mock_file):
    transactions = get_transactions_data("data/operations.json")

    assert transactions == []
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="not a json")
def test_get_transactions_data_error_file(mock_file):
    transactions = get_transactions_data("data/operations.json")

    assert transactions == []
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="1")
def test_get_transactions_data_not_list(mock_file):
    transactions = get_transactions_data("data/operations.json")

    assert transactions == []
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")
