import json

def get_transactions_data(path: str) -> list[dict]:
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    try:
        if path:
            with open (path, 'r', encoding='utf-8') as json_file:
                transactions_data = json.load(json_file)
                if isinstance(transactions_data, list):

                    return transactions_data
        return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


if __name__ == '__main__':
    print(get_transactions_data("C:/pythonProject/Bank_App/data/operations.json"))