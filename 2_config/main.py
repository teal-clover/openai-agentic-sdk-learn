import logging
import os

from agents import (
    enable_verbose_stdout_logging,
    set_default_openai_key,
    set_tracing_disabled,
)
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")
TRACING_KEY = os.getenv("TRACING_KEY")
assert OPEN_AI_KEY is not None and TRACING_KEY is not None
set_default_openai_key(OPEN_AI_KEY)
set_tracing_disabled(True)

enable_verbose_stdout_logging()

logger = logging.getLogger(
    "openai.agents"
)  # or openai.agents.tracing for the Tracing logger

# To make all logs show up
logger.setLevel(logging.DEBUG)
# To make info and above show up
logger.setLevel(logging.INFO)
# To make warning and above show up
logger.setLevel(logging.WARNING)
# etc

# You can customize this as needed, but this will output to `stderr` by default
logger.addHandler(logging.StreamHandler())
