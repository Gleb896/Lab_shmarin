# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as input_c:
        need_to_read = csv.DictReader(input_c)

        values = [row for row in need_to_read]

    with open(OUTPUT_FILENAME, "w") as output_j:
        json.dump(values, output_j, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
