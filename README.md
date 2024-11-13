# Bank App

## Описание:

Проект Bank App - это виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка:

Клонируйте репозиторий:
```
git clone https://github.com/MikhailLemdyanov/homework-10-1
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

## Автор проекта:

Михаил Лемдянов
