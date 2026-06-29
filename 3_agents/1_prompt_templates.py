import asyncio
import os

from agents import Agent, RunConfig, Runner, set_default_openai_key
from dotenv import load_dotenv

load_dotenv()
OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")
assert type(OPEN_AI_KEY) is str
set_default_openai_key(OPEN_AI_KEY)

agent = Agent(
    name="Prompted assistant",
    prompt={
        "id": "pmpt_69caaed026f8819386033bb17e64fcd00bffb5998a9301cc",
        "version": "1",
        "variables": {"poem_style": "haiku"},
    },
)


async def main():
    result = await Runner.run(
        agent,
        "When rome fall (remember propt)",
        run_config=RunConfig(trace_include_sensitive_data=True),
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
