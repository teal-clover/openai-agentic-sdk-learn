import asyncio
import os
from dataclasses import dataclass

from agents import (
    Agent,
    GenerateDynamicPromptData,
    Prompt,
    Runner,
    set_default_openai_key,
)
from dotenv import load_dotenv

load_dotenv()
OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")
assert type(OPEN_AI_KEY) is str
set_default_openai_key(OPEN_AI_KEY)


async def main():
    from agents import Agent
    from pydantic import BaseModel

    class CalendarEvent(BaseModel):
        name: str
        date: str
        participants: list[str]

    agent = Agent(
        name="Calendar extractor",
        instructions="Extract calendar events from text",
        output_type=CalendarEvent,
    )
    result = await Runner.run(
        agent,
        "Say hello to Mr John, which we will meet next tuesday. Today is tuesday Mar 31 26",
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
