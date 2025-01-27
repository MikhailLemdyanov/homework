import re
from typing import Any


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
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    search_result = []
    for transaction in list_of_transactions:
        if "description" in transaction and search_str:
            if re.search(pattern, transaction["description"]):
                search_result.append(transaction)
        else:
            return []
    return search_result


def count_by_description(list_of_transactions: list[dict], category_list: list[str]) -> dict:
    """Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций и
    возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории
    """
    search_result = {}

    if category_list:
        for category in category_list:
            pattern = re.compile(re.escape(category), flags=re.IGNORECASE)

            category_counter = 0

            for transaction in list_of_transactions:
                if re.search(pattern, transaction["description"]):
                    category_counter += 1
                    search_result[category] = category_counter
    else:
        raise Exception("Список категорий пустой")

    return search_result
