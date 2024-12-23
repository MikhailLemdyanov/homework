# Bank App

## Описание:

Проект Bank App - это виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка:

Клонируйте репозиторий:
```
git clone https://github.com/MikhailLemdyanov/homework
```

## Использование:

1. Запустите основной файл:
```
python main.py
```
2. Введите номер Вашей банковской карты.
3. Введите номер Вашего счета.

## Реализованные функции:

1. Функция, которая принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX 
2. Функция, которая принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX
3. Функция, которая принимает на вход строку формата Visa Platinum 7000 7922 8960 6361, или Maestro 7000 7922 8960 6361, или Счет 73654108430135874305, для маскировки номера карты/счета используются ранее написанные функции из модуля masks
4. Функция, которая принимает на вход строку и отдает корректный результат в формате 11.07.2018
5. Функция, которая принимает на вход список словарей с данными о банковских операциях и параметр state, и возвращает новый список, содержащий только те словари, у которых ключ state содержит переданное в функцию значение
6. Функция, которая принимает на вход список словарей и параметр порядка сортировки, и возвращает новый список, в котором исходные словари отсортированы по дате
7. Функция, которая принимает на вход список словарей, представляющих транзакции и возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)
8. Функция, которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
9. Функция, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты
10. Декоратор, который автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки
11. Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
12. Функция, которая принимает на вход транзакцию и возвращает сумму транзакции
13. Созданы логеры для модулей masks.py и utils.py
14. Функция для считывания финансовых операций из CSV
15. Функция для считывания финансовых операций из Excel

## Информация о тестировании:

1. Написаны тесты ко всем функциям проекта
2. Модули тестируются в отдельных тестовых файлах
3. Функциональный код покрыт тестами более чем на 80%
4. При запуске тестов командой pytest все тесты завершаются успешно
5. В репозитории есть папка с отчетом покрытия тестами в формате HTML

## Автор проекта:

Михаил Лемдянов
