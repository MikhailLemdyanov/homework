import pytest

@pytest.fixture
def transaction_for_conversion():
    return {
        "id": 361044570,
        "state": "EXECUTED",
        "date": "2018-03-02T02:03:11.563721",
        "operationAmount": {"amount": "5", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 96008924215040031147",
        "to": "Счет 30377212495530283001",
    }


@pytest.fixture
def result_of_conversion():
    return """{
  "date": "2018-02-22",
  "historical": "",
  "info": {
    "rate": 148.972231,
    "timestamp": 1519328414
  },
  "query": {
    "amount": 25,
    "from": "USD",
    "to": "RUB"
  },
  "result": 531.307615,
  "success": true
}"""


@pytest.fixture
def result_of_conversion_without_result():
    return """{
  "date": "2018-02-22",
  "historical": "",
  "info": {
    "rate": 148.972231,
    "timestamp": 1519328414
  },
  "query": {
    "amount": 25,
    "from": "USD",
    "to": "RUB"
  },
  "success": true
}"""


@pytest.fixture
def transaction_for_conversion_invalid():
    return {
        "id": 361044570,
        "state": "EXECUTED",
        "date": "2018-03-02T02:03:11.563721",
        "operationAmount": {
            "amount": "5",
        },
        "description": "Перевод организации",
        "from": "Счет 96008924215040031147",
        "to": "Счет 30377212495530283001",
    }

@pytest.fixture
def transactions_list():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
