import asyncio
import os

from agents import (
    Agent,
    OpenAIChatCompletionsModel,
    Runner,
    function_tool,
    set_default_openai_key,
    set_default_openai_responses_transport,
)
from agents.tool import ToolSearchTool
from dotenv import load_dotenv
from openai import AsyncOpenAI

set_default_openai_responses_transport("websocket")

load_dotenv()
OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")
assert type(OPEN_AI_KEY) is str
set_default_openai_key(OPEN_AI_KEY)


@function_tool(defer_loading=True)
def get_weather(location: str):
    return "Weather is nice!"


# 1. Define a specialist using the ChatCompletions shape
# This shape DOES NOT support ToolSearchTool [2, 3].
specialist = Agent(
    name="Specialist",
    model=OpenAIChatCompletionsModel(model="gpt-5.4", openai_client=AsyncOpenAI()),
    tools=[ToolSearchTool(), get_weather],
    instructions="You are a specialist.",
)

# 2. Define a triage agent using the default Responses shape
# We add a ToolSearchTool, which is a Responses-only feature [4, 5].
triage_agent = Agent(
    name="Triage",
    instructions="Greet back imediately.",
    model="gpt-5.4",
    handoffs=[specialist],
)


async def main():
    # 3. Run the orchestration
    # The SDK recommends using a single model shape for each workflow because
    # different shapes support different features [Sources/Chat History].
    try:
        result = await Runner.run(
            triage_agent,
            input="Hello. Can you ask specialist what's the weather in romania?",
        )
        print(result.final_output)
    except Exception as e:
        # This will fail when the specialist agent's turn is reached
        # because the ChatCompletions model rejects the ToolSearchTool.
        print(f"Workflow failed as expected: {e}")


if __name__ == "__main__":
    asyncio.run(main())
