import json
from pathlib import Path

def read_products_from_json(file_path):
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        products = json.load(file)

    names = [product["name"] for product in products]
    return names