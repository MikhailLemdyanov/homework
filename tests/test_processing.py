from typing import Any

import pytest

from src.processing import count_by_description, filter_by_state, search_by_description, sort_by_date


@pytest.fixture()
def my_list_of_dict() -> list[dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "id_state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(my_list_of_dict: list[dict[str, Any]], id_state: str, expected: list[dict[str, Any]]) -> None:
    assert filter_by_state(my_list_of_dict, id_state) == expected


def test_sort_by_date(my_list_of_dict: list[dict[str, Any]]) -> None:
    assert sort_by_date(my_list_of_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_search_by_description(
    transactions_list: list[dict[str, Any]], result_transactions_filter: list[dict[str, Any]]
) -> None:
    result = search_by_description(transactions_list, "Счет")

    assert result == result_transactions_filter


def test_search_by_description_empty_list(transactions_list_empty: list[dict[str, Any]]) -> None:
    result = search_by_description(transactions_list_empty, "Счет")

    assert result == []


def test_search_by_description_empty_search(transactions_list: list[dict[str, Any]]) -> None:
    result = search_by_description(transactions_list, "")

    assert result == []


def test_search_by_description_invalid_search(transactions_list: list[dict[str, Any]]) -> None:
    result = search_by_description(transactions_list, "привет")

    assert result == []


def test_search_by_description_without_transactions(random_list: list[dict[str, Any]]) -> None:
    result = search_by_description(random_list, "пупупу")

    assert result == []


def test_count_by_description(transactions_list: list[dict[str, Any]], category_list: list[str]) -> None:
    result = count_by_description(transactions_list, category_list)

    assert result == {"Перевод организации": 2, "Перевод с карты на карту": 1, "Перевод со счета на счет": 2}
