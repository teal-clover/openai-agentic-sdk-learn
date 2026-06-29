import asyncio
import os

from agents import (
    Runner,
    set_default_openai_key,
)
from dotenv import load_dotenv

load_dotenv()
OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")
assert type(OPEN_AI_KEY) is str
set_default_openai_key(OPEN_AI_KEY)


async def main():
    from agents import Agent, ModelSettings

    english_agent = Agent(
        name="English agent",
        instructions="You only speak English",
        model="gpt-4.1",
        model_settings=ModelSettings(
            temperature=0.1,
            extra_args={"service_tier": "flex", "user": "user_12345"},
        ),
    )
    result = await Runner.run(
        english_agent,
        "Hello",
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
