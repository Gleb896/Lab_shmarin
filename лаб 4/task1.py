import json

FILENAME = "input.json"


def task() -> float:
    """
    Функция для вычисления суммы произведений (score * weight).
    """
    with open(FILENAME, 'r') as input_f:
        data = json.load(input_f)

    multiple = sum([items['score'] * items['weight'] for items in data])

    return round(multiple, 3)


print(task())
