import subprocess
from pathlib import Path
# from ..packaged_meme import packaged_meme

# SCRAPED_MEME=packaged_meme()
# SCRAPED_MEME_TITLE=SCRAPED_MEME["title"]

GIT_BASH_FILE=Path(__file__).parent / "gitcron.sh"

# run bash script . pass the title as the commit message

def update_storage_github(MEME_TITLE: str):
    subprocess.run(["bash", str(GIT_BASH_FILE), MEME_TITLE])