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
    from typing import Any, List

    from agents import (
        Agent,
        FunctionToolResult,
        RunContextWrapper,
        Runner,
        function_tool,
    )
    from agents.agent import ToolsToFinalOutputResult

    @function_tool
    def get_weather(city: str) -> str:
        """Returns weather info for the specified city."""
        return f"The weather in {city} is sunny"

    def custom_tool_handler(
        context: RunContextWrapper[Any], tool_results: List[FunctionToolResult]
    ) -> ToolsToFinalOutputResult:
        """Processes tool results to decide final output."""
        for result in tool_results:
            if result.output and "sunny" in result.output:
                return ToolsToFinalOutputResult(
                    is_final_output=True, final_output=f"Final weather: {result.output}"
                )
        return ToolsToFinalOutputResult(is_final_output=False, final_output=None)

    agent = Agent(
        name="Weather Agent",
        instructions="Retrieve weather details.",
        tools=[get_weather],
        tool_use_behavior=custom_tool_handler,
    )

    result = await Runner.run(
        agent,
        "What's the weather in Chicago?",
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
