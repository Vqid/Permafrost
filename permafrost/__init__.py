import os
from pathlib import Path
from dotenv import load_dotenv
from .db import Database
from .utils.helpers import random_color

load_dotenv()

__token__ = os.environ.get('BOT_TOKEN')
DEFAULT_GUILD = os.environ.get('DEFAULT_GUILD')
PREFIX = "pf?"
__palette__ = (
    0x4C5CF6,
    0x4275D4,
    0x54B1EB,
    0x42C2D4,
    0x4CF6DC
)

__version__ = "0.1.0.dev0"
__author__ = "vqid"
__username__ = "Permafrost#5353"
_static = Path("./data/static")
_dynamic = Path("./data/dynamic")