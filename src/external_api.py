import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def currency_convert(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    try:
        currency = transaction["operationAmount"]["currency"]["code"]
        amount = float(transaction["operationAmount"]["amount"])

        if currency == "RUB":
            return amount
        else:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
            key = {"apikey": API_KEY}
            response = requests.get(url, headers=key)
            if response.status_code == 200:
                info = response.json()
                if "result" in info:
                    return float(info["result"])
                else:
                    raise ValueError("Недостаточно данных для конвертации")
            else:
                raise Exception(f"Запрос не успешен: {response.reason}")
    except KeyError:
        raise KeyError("Нет данных для конвертации")
