import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]

    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_file:
        for line in output_file:
            print(line, end="")