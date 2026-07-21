from pathlib import Path
from dotenv import load_dotenv
import os


ENV_PATH=Path(__file__).parent.parent / ".env"

load_dotenv(ENV_PATH)

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
