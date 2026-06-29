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
    @dataclass
    class PromptContext:
        prompt_id: str
        poem_style: str

    async def build_prompt(data: GenerateDynamicPromptData) -> Prompt:
        ctx: PromptContext = data.context.context
        return {
            "id": ctx.prompt_id,
            "version": "1",
            "variables": {"poem_style": ctx.poem_style},
        }

    agent = Agent(name="Prompted assistant", prompt=build_prompt)
    result = await Runner.run(
        agent,
        "Say hello",
        context=PromptContext(
            prompt_id="pmpt_69caaed026f8819386033bb17e64fcd00bffb5998a9301cc",
            poem_style="limerick",
        ),
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
