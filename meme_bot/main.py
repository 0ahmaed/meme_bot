import pprint

from .SCRAPER.packaged_meme import packaged_meme
from .BOT.discord_sender import DiscordSender
from .BOT.config import DISCORD_WEBHOOK_URL
from .SCRAPER.STORAGE.latest_meme_replacer import meme_title_replacer

SCRAPED_MEME=packaged_meme()
SCRAPED_MEME_TITLE=SCRAPED_MEME["title"]

def main():
    if meme_title_replacer(SCRAPED_MEME_TITLE):
        sender = DiscordSender(DISCORD_WEBHOOK_URL, SCRAPED_MEME)
        sender.send_meme(SCRAPED_MEME)
    else:
        sender = DiscordSender(DISCORD_WEBHOOK_URL, SCRAPED_MEME)
        sender.default_message()

if __name__ == "__main__":
    main()
