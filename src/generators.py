from typing import Any, Generator


def filter_by_currency(list_of_transaction: list[dict[str, Any]], currency: str) -> Generator[Any]:
    """Функция принимает на вход список словарей, представляющих транзакции и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)"""
    return (x for x in list_of_transaction if x["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(list_of_transaction: list[dict[str, Any]]) -> Generator[Any]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание
    каждой операции по очереди"""
    for x in list_of_transaction:
        yield x.get("description")


def card_number_generator(start: int, stop: int) -> Generator[Any]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты"""
    for num in range(start, stop):
        card_number = str(num)
        while len(card_number) < 16:
            card_number = "0" + card_number
        result = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        yield result
