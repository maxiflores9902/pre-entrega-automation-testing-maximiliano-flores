import csv
import pathlib


def read_csv_login(path):
    path_csv = pathlib.Path(path)
    data = []
    with open(path_csv, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            works = row["works"].lower() == "true"
            data.append((row["user"], row["password"], works))
    return data
