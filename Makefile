.PHONY: run

run:
	cd meme_bot && . ./.venv/bin/activate && cd .. && python3 -m meme_bot.main

git:
	bash git.sh

test:
	cd meme_bot && . ./.venv/bin/activate && cd .. && python3 -m meme_bot.testing_script

discord:
	cd meme_bot && . ./.venv/bin/activate && cd .. && python3 -m meme_bot.BOT.discord_sender

storage:
	cd meme_bot && . ./.venv/bin/activate && cd .. && python3 -m meme_bot.SCRAPER.STORAGE.meme_duplication_checker

dupe:
	cd meme_bot && . ./.venv/bin/activate && cd .. && python3 -m meme_bot.SCRAPER.STORAGE.latest_meme_replacer
cron:
	python3 -m meme_bot.main