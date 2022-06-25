import os
from pathlib import Path
from dotenv import load_dotenv
from .db import Database

load_dotenv()

__token__ = os.environ.get('BOT_TOKEN')
DEFAULT_GUILD = os.environ.get('DEFAULT_GUILD')

__version__ = "0.1.0.dev0"
__author__ = "vqid"
__username__ = "Permafrost#5353"
_static = Path("./data/static")
_dynamic = Path("./data/dynamic")