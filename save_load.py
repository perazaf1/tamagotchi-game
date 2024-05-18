import json
import os

save_file = "save_data.json"

def save_game(data):
    with open(save_file, 'w') as file:
        json.dump(data, file)

def load_game():
    if os.path.exists(save_file):
        with open(save_file, 'r') as file:
            return json.load(file)
    return None
