from typing import Any


def filter_by_state(list_of_dictionaries: list[dict[str, Any]], id_state: str = "EXECUTED") -> Any:
    """
    Функция, которая возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению
    """
    return [dictionary for dictionary in list_of_dictionaries if dictionary.get("state") == id_state]
