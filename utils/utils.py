import json
from datetime import datetime


def loads_json(filename):
    """считывает джейсон файл"""
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def _converts_date(date):
    """конвертирует дату"""
    return datetime.fromisoformat(date).strftime('%d.%m.%Y')


def _hides_card_number(card_number):
    """маскирует номер карты"""
    first_digits = card_number[:4]
    second_digits = card_number[4:6]+'**'
    last_digits = card_number[-4:]
    other_digits = '****'
    hidden_card_number = first_digits + ' ' + second_digits + ' ' + other_digits + ' ' + last_digits
    return hidden_card_number


def _hides_account(account):
    """маскирует номер счета"""
    last_digits = account[-4:]
    return '**' + last_digits


def _checks_card_or_account(order):
    """проверяет номер счета или номер карты"""
    if len(order) == 16:
        return _hides_card_number(order)
    return _hides_account(order)


def shows_last_operations(operations):
    """выводит данные"""
    for operation in operations:
        from__ = None
        date = _converts_date(operation['date'])
        description = operation['description']
        if operation.get('from'):
            from_ = operation['from'].split()
            from_name = from_[:-1]
            from_order = ' '.join(from_name) + ' ' + _checks_card_or_account(from_[-1])
            from__ = from_order
        to_ = operation['to'].split()
        to_name = to_[:-1]
        to = ' '.join(to_name) + ' ' + _hides_account(to_[-1])
        operationAmount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        print(f'{date} {description}')
        if from__ is not None:
            print(f'{from__} {to}')
        else:
            print(to)
        print(f'{operationAmount} {currency}\n')


