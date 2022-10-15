from services.Lagrange import Lagrange
import json
from pathlib import Path


def calculate(data):
    lagrange = Lagrange(data=data)
    lagrange.get_polinomyals()
    fnx_simplified = lagrange.get_fnx_simplified()
    fnx_beauty = lagrange.get_fnx_beauty()
    
    return fnx_simplified, fnx_beauty


def do_operations(json_data, f):
    for idx, i in enumerate(json_data):
        if "results" not in json_data[idx]:
            print(i["data"])
            fnx_simplified, fnx_beauty = calculate(i["data"])
            
            json_data[idx]["results"] = {
                "fn(x)": fnx_beauty, 
                "simplified_fn(x)": str(fnx_simplified)
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
