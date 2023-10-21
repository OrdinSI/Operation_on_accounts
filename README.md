# **Операции по счетам**

Проект "Операции по счетам" представляет собой решение для вывода списка последних пяти успешных банковских операций клиента в удобном формате. Этот проект разработан в рамках курсового проекта "Основы backend-разработки".

## **О задаче**

IT-отдел крупного банка разрабатывает новую функциональность для личного кабинета клиента - виджет "Операции по счетам". Задача заключается в реализации алгоритма на бэкенде для подготовки данных, которые будут отображаться в этом виджете.

## **Задача**
Задача заключается в реализации функции, которая выводит на экран список из пяти последних выполненных операций клиента в следующем формате:

<дата перевода> <описание перевода>\
<откуда> -> <куда>\
<сумма перевода> <валюта>

#### Пример вывода для одной операции:

14.10.2018 Перевод организации\
Visa Platinum 7000 79** **** 6361 -> Счет **9638\
82771.72 руб.

## **Выполненные задачи**
Реализован вывод последних 5 успешных операций.\
Операции разделены пустой строкой.\
Дата перевода представлена в формате ДД.ММ.ГГГГ.\
Самые последние операции располагаются в верхней части списка.\
Номер карты замаскирован и отображается как XXXX XX** **** XXXX.\
Номер счета замаскирован и отображается как **XXXX.\
