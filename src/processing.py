from typing import Any


def filter_by_state(list_of_dictionaries: list[dict[str, Any]], id_state: str = "EXECUTED") -> Any:
    """
    Функция, которая возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению
    """
    return [dictionary for dictionary in list_of_dictionaries if dictionary.get("state") == id_state]


def sort_by_date(list_of_dictionaries: list[dict[str, Any]], reverse_list: bool = True) -> list[dict[str, Any]]:
    """Функция, которая возвращает список словарей отсортированный по дате"""

    sorted_list_of_dictionaries = sorted(list_of_dictionaries, key=lambda x: x["date"], reverse=reverse_list)

    return sorted_list_of_dictionaries
