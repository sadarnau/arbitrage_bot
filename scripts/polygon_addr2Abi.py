import os
from os import path
from dotenv import load_dotenv
import requests
import json

load_dotenv()


def get_contract(contract_addr: str):
    res = requests.get(
        "https://api.polygonscan.com/api?module=contract&action=getabi&address="
        + contract_addr
        + "&apikey="
        + os.getenv("POLYGON_API_KEY")
    )

    jsoned = json.loads(res.text)

    if jsoned["status"] != "1":
        print(
            "someting went wrong with " + contract_addr + ":",
            jsoned["result"],
        )
        return 1

    with open("db/" + contract_addr, "w") as f:
        f.write(jsoned["result"])

    return 0


def check_db(contract_addr: str):
    if path.exists("db/" + contract_addr):
        print(contract_addr + " already in db!")
        return 0
    else:
        print(contract_addr + " not found in db, now downloading")
        return 1


if check_db("test"):
    get_contract("test")
