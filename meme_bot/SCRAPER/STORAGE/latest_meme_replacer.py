import json

from .meme_duplication_checker import title_duplication_checker
from pathlib import Path

JSON_FILE = Path(__file__).parent / "meme_storage.json"


def meme_title_replacer(scraped_title:str)->bool:
    #if the title is the same as the one in storage, return False otherwise return True
    if title_duplication_checker(scraped_title):
        return False
    else:
        with open(JSON_FILE, "w") as file:
            json.dump({"title": scraped_title}, file)
        return True
