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
TRACING_KEY = os.getenv("TRACING_KEY")
print(OPEN_AI_KEY)
assert OPEN_AI_KEY is not None and TRACING_KEY is not None
set_default_openai_key(OPEN_AI_KEY)
# set_tracing_disabled(True)
# In terminal:
# export OPENAI_ORG_ID="org_..." - must be defined first
# export OPENAI_PROJECT_ID="proj_..." - same
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
