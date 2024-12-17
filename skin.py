import json

def write_in_file(data):
    with open("player_info.json", 'w', encoding='utf8')as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def read_from_file():
    try:
        with open("player_info.json", 'r', encoding='utf8')as file:
            data = json.load(file)
            return data
    except:
        data = {
            "кількість монет": 0,
            "скін": "rocket.png"
        }
        return data