import csv

import pandas as pd


def get_csv_data(csv_file_path: str) -> list:
    """Функция для считывания финансовых операций из CSV и возврата списка словарей с транзакциями"""
    try:
        with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:
            result_dict_from_csv = csv.DictReader(csv_file, delimiter=";")

            return list(result_dict_from_csv)

    except Exception:
        return []


def get_excel_data(excel_file_path: str) -> list:
    """Функция для считывания финансовых операций из Excel и возврата списка словарей с транзакциями"""
    try:
        df = pd.read_excel(excel_file_path)

        if isinstance(df, pd.DataFrame) and not df.empty:
            return df.to_dict(orient="records")

        return []

    except FileNotFoundError:
        return []

    except Exception:
        return []


if __name__ == "__main__":
    print(get_csv_data("C:/pythonProject/Bank_App/data/transactions.csv"))
    print(get_excel_data("C:/pythonProject/Bank_App/data/transactions_excel.xlsx"))
