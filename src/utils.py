import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../Bank_App/logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_data(path: str) -> list[dict]:
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.info("Открытие json-файла")
        if path:
            logger.info("Json-файл открыт")
            with open(path, "r", encoding="utf-8") as json_file:
                logger.info("Загрузка данных из json-файла и преобразование в Python-объект.")
                transactions_data = json.load(json_file)
                logger.info("Проверка: является ли содержимое файла списком.")
                if isinstance(transactions_data, list):
                    logger.info("Содержимое файла является списком.")
                    logger.info("Данные в формате Python-объекта получены успешно.")
                    return transactions_data
        logger.error("Файл отсутствует")
        return []
    except FileNotFoundError:
        logger.error(f"Файл по пути {json_file} не найден.")
        return []
    except json.JSONDecodeError:
        logger.error("Данные из json-файла не соответствует синтаксису JSON или содержат ошибочные данные")
        return []


if __name__ == "__main__":
    print(get_transactions_data("C:/pythonProject/Bank_App/data/operations.json"))
