import asyncio
import logging
import os

from agents import (
    Agent,
    RunConfig,
    Runner,
    enable_verbose_stdout_logging,
    set_default_openai_key,
    set_tracing_disabled,
)
from dotenv import load_dotenv

load_dotenv()
OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")

logger = logging.getLogger(
    "openai.agents.tracing"
)  # or openai.agents.tracing for the Tracing logger
enable_verbose_stdout_logging()
# logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

# # To make all logs show up
logger.setLevel(logging.DEBUG)
# # To make info and above show up
# logger.setLevel(logging.INFO)
# # To make warning and above show up
# logger.setLevel(logging.WARNING)
# # etc

# You can customize this as needed, but this will output to `stderr` by default
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

agent = Agent(
    name="History Tutor",
    instructions="You answer history questions clearly and concisely.",
)


async def main():
    result = await Runner.run(
        agent,
        "When did the Roman Empire fall?",
        run_config=RunConfig(trace_include_sensitive_data=True),
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
