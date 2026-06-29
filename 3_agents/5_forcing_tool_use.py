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
    from agents import Agent, Runner, function_tool
    from agents.agent import StopAtTools

    @function_tool
    def get_weather(city: str) -> str:
        """Returns weather info for the specified city."""
        return f"The weather in {city} is sunny"

    @function_tool
    def sum_numbers(a: int, b: int) -> int:
        """Adds two numbers."""
        return a + b

    agent = Agent(
        name="Stop At Stock Agent",
        instructions="Get weather or sum numbers.",
        tools=[get_weather, sum_numbers],
        tool_use_behavior=StopAtTools(stop_at_tool_names=["get_weather"]),
    )
    result = await Runner.run(
        agent,
        "Say hello to Mr John, which we will meet next tuesday in Chicago. Today is tuesday Mar 31 26",
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
