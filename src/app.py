from services.Lagrange import Lagrange
import json
from pathlib import Path


def calculate(data):
    lagrange = Lagrange(data=data)
    lagrange.get_polinomyals()
    fnx = lagrange.get_px()
    simplified_fnx = lagrange.get_px_simplified()
    return fnx, simplified_fnx


def do_operations(json_data, f):
    for idx, i in enumerate(json_data):
        if "results" not in json_data[idx]:
            print(i["data"])
            fnx, simplified_fnx = calculate(i["data"])
            
            json_data[idx]["results"] = {
                "fn(x)": str(fnx), 
                "simplified_fn(x)": str(simplified_fnx)
            }

            f.seek(0)
            json.dump(json_data, f, indent=4)
            f.truncate()


def update_date_file():
    curret_path = Path(__file__).parent.resolve() 
    data = curret_path / "data.json"
    with open(data, "r+") as f:
        json_data = json.load(f)
        do_operations(json_data, f)


if __name__ == "__main__":
    update_date_file()
