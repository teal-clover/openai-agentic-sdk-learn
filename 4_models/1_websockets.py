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
    from agents import Agent, OpenAIProvider, RunConfig, Runner

    provider = OpenAIProvider(
        use_responses_websocket=True,
        # Optional; if omitted, OPENAI_WEBSOCKET_BASE_URL is used when set.
        # websocket_base_url="wss://your-proxy.example/v1",
    )

    agent = Agent(name="Assistant")
    result = await Runner.run(
        agent,
        "Hello",
        run_config=RunConfig(model_provider=provider),
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
