import asyncio
import os

from agents import set_default_openai_key, set_default_openai_responses_transport
from dotenv import load_dotenv

set_default_openai_responses_transport("websocket")

load_dotenv()
OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")
assert type(OPEN_AI_KEY) is str
set_default_openai_key(OPEN_AI_KEY)


async def main():
    from agents import Agent, MultiProvider, RunConfig, Runner

    provider = MultiProvider(
        openai_base_url="https://openrouter.ai/api/v1",
        openai_api_key=OPEN_AI_KEY,
        openai_use_responses_websocket=True,
        openai_prefix_mode="model_id",
        unknown_prefix_mode="model_id",
    )

    agent = Agent(
        name="Assistant",
        instructions="Be concise.",
        model="openai/gpt-4.1",
    )

    result = await Runner.run(
        agent,
        "Hello",
        run_config=RunConfig(model_provider=provider),
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
