import os

from processing import filter_by_state, sort_by_date
from reader import get_csv_data, get_excel_data
from generators import filter_by_currency
from processing import search_by_description
from generators import transaction_descriptions
from widget import get_date, mask_account_card
from utils import get_transactions_data


def main():
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой"""
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями')

    while True:
        print("""Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла""")

        file_selection = input('Введите номер пункта(1-3): ')

        if file_selection == '1':
            print('Для обработки выбран JSON-файл.')
            transactions_file = get_transactions_data(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data"
                                                      f"\\operations.json")
            break
        elif file_selection == '2':
            print('Для обработки выбран CSV-файл.')
            transactions_file = get_csv_data(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data"
                                                      f"\\transactions.csv")
            break
        elif file_selection == '3':
            print('Для обработки выбран XLSX-файл.')
            transactions_file = get_excel_data(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data"
                                                      f"\\transactions_excel.xlsx")
            break
        else:
            print('Введен некорректный номер')
            continue

    print("""Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

    while True:
        status_selection = input('Введите статус: ').upper()

        if status_selection in ['EXECUTED', 'CANCELED', 'PENDING']:
            filtered_transactions = filter_by_state(transactions_file, status_selection)
            break
        else:
            print(f'Статус операции {status_selection} недоступен.')

    while True:
        print('Отсортировать операции по дате? Да/Нет')
        user_input_date = input('Введите Да/Нет:').lower()

        if user_input_date == 'да':
            print('Отсортировать по возрастанию или по убыванию? ')
            user_input_sort = input('Введите по возрастанию/по убыванию: ').lower()
            if user_input_sort == 'по возрастанию':
                sorted_transactions = sort_by_date(filtered_transactions, False)
                break
            elif user_input_sort == 'по убыванию':
                sorted_transactions = sort_by_date(filtered_transactions, True)
                break
            else:
                print('Введен некорректный ответ.')
                continue
        elif user_input_date == 'нет':
            sorted_transactions = filtered_transactions
            break
        else:
            print('Введен некорректный ответ. Введите "Да" или "Нет".')

    while True:
        print('Выводить только рублевые транзакции? Да/Нет')
        user_currency_filter = input('Введите да/нет: ').lower()

        if user_currency_filter == 'да':
            transactions_by_currency = list(filter_by_currency(sorted_transactions, 'RUB'))
            break
        elif user_currency_filter == 'нет':
            transactions_by_currency = sorted_transactions
            break
        else:
            print('Введен неверный ответ. Введите "Да" или "Нет"')
            continue

    print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')

    while True:
        description_filter = input('Введите да/нет: ').lower()

        if description_filter == 'да':
            user_search = input('Введите слово для поиска по описанию: ')
            result = list(search_by_description(transactions_by_currency, user_search))
            break
        elif description_filter == 'нет':
            result = list(transactions_by_currency)
            break
        else:
            print('Введен неверный ответ. Введите "Да" или "Нет"')
            continue

    if result:
        print('Распечатываю итоговый список транзакций...')
        print(f'Всего банковских операций в выборке: {len(result)}')

        for transaction in result:

            description = next(transaction_descriptions(result), 'Описание отсутствует')
            print(f'{get_date(transaction['date'])} {description}')

            if transaction.get('from') and transaction.get('to'):
                print(f'{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['from'])}')

            elif not transaction.get('from') and transaction.get('to'):
                print({mask_account_card(transaction['to'])})

            if file_selection == '1':
                print(
                    f'Сумма: {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}\n'
                )
            elif file_selection == '2' or file_selection == '3':
                print(f'Сумма: {transaction['amount']} {transaction['currency_name']}\n')

            else:
                print('Не найдено ни одной транзакции, подходящей под Ваши условия фильтрации')

        return result



if __name__ == "__main__":
    main()







