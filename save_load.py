import json
import os
import abs_path



save_file = "save_data.json"  # Define the name of the save file

def save_game(data):
    # Save game data to a JSON file
    with open(save_file, 'w') as file:
        json.dump(data, file)

def load_game():
    # Load game data from the JSON file if it exists
    if os.path.exists(save_file):
        with open(save_file, 'r') as file:
            return json.load(file)
    return None  # Return None if the save file does not exist


file_path = abs_path.abs_path("save_data.json")
def delete_game():
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted save file at {file_path}")
        else:
            print(f"No save file found at {file_path}")
    except Exception as e:
        print(f"Error deleting save file: {e}")

    
