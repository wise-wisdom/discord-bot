import json


def get_token() -> str:
    with open("./config.json", mode="r", encoding="utf-8") as fp:
        configs = json.load(fp)

    return configs.get("token")