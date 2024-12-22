from unittest.mock import mock_open, patch
from src.reader import get_csv_data, get_excel_data
import pandas as pd


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n"
    "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n"
    "3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту",
)
def test_get_csv_data(mock_file, csv_data_result):
    transactions = get_csv_data("../data/transactions.xlsx")

    assert transactions == csv_data_result
    mock_file.assert_called_once_with("../data/transactions.xlsx", mode="r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_csv_invalid(mock_file):
    transactions = get_csv_data("../data/transactions.xlsx")

    assert transactions == []
    mock_file.assert_called_once_with("../data/transactions.xlsx", mode="r", encoding="utf-8")


def test_read_csv_invalid_path():
    transactions = get_csv_data("some/invalid/path")

    assert transactions == []


def test_read_csv_not_path():
    transactions = get_csv_data("")

    assert transactions == []

@patch("pandas.read_excel")
def test_get_excel(mock_read_excel, excel_data, excel_data_result):
    mock_read_excel.return_value = pd.DataFrame(excel_data)

    result = get_excel_data("../data/transactions.xlsx")
    assert result == excel_data_result


def test_get_excel_no_path():
    result = get_excel_data("")

    assert result == []


def test_get_excel_invalid_path():
    result = get_excel_data("files/some_file.xlsx")

    assert result == []


@patch("pandas.read_excel")
def test_get_excel_empty(mock_read_excel):
    mock_read_excel.return_value = ""

    result = get_excel_data("files/some_file.xlsx")
    assert result == []