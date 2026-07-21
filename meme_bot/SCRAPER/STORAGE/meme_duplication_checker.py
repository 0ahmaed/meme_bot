import json
from pathlib import Path
JSON_FILE = Path(__file__).parent / "meme_storage.json"


def load_title():
    try:

        with open(JSON_FILE, "r") as file:
            data = json.load(file)
        return data
    
    except Exception as e:

        print(f"An error occurred: {e}")
        return "Failure ❎"

def title_duplication_checker(scraped_title:str):
    storage_title = load_title()

    if storage_title["title"] == scraped_title:
        return True
    return False
    

        

if __name__ == "__main__":
    print(title_duplication_checker("This Is Fine"))
    