from typing import Any
import re
from collections import Counter



def filter_by_state(list_of_dictionaries: list[dict[str, Any]], id_state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Функция, которая возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению
    """
    return [dictionary for dictionary in list_of_dictionaries if dictionary.get("state") == id_state]


def sort_by_date(list_of_dictionaries: list[dict[str, Any]], reverse_list: bool = True) -> list[dict[str, Any]]:
    """Функция, которая возвращает список словарей отсортированный по дате"""

    sorted_list_of_dictionaries = sorted(list_of_dictionaries, key=lambda x: x["date"], reverse=reverse_list)
    return sorted_list_of_dictionaries


def search_by_description(list_of_transactions: list[dict], search_str: str) -> list[dict]:
    """Функция, которая принимает список словарей с данными о банковских операциях и строку поиска
    и возвращает список словарей, у которых в описании есть данная строка"""
    search_result = []
    for transaction in list_of_transactions:
        if re.search(search_str, list_of_transactions['description'], flags=re.IGNORECASE):
            search_result.append(transaction)
    return search_result


def count_by_description(list_of_transactions: list[dict], description_list: list[str]) -> list[dict]:
    """Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций и
     возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории"""
    list_for_count = []
    for description in description_list:
        for transaction in list_of_transactions:
            if transaction['description'] == description.title():
                list_for_count.append(transaction['description'])
    count_result = Counter(list_for_count)
    return count_result

