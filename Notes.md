# Agents

## Quickstart

Actors and their domains

- Agents - the rulers of the agentic domain.
  - Agent loop - not sure if actor, or action that actor does.
  - Runner - has API page
    - Can use session
      - Can resuse *OPENAI server-managed state*. Idk what is that. (Running agents will explain.)
  - RunResult - same API page, gonna skip for tutorial time.
    - Can move response back to input list. Provides full controller to the runner over the text.
- Agent as tools and Handoffs
  - Agent as tools - orchestrator agent still decides what to do with data
  - Handoffs - full responsibility to other agent
- Guardrails
- Tracing - tracing and evaluation, thanks to OpenAI suite
- Tools - functions that have reign over the backend code, may be invoked by agents.
  - Pydantic schemas - provide tool the ability to define what will come in and out.
  - MCP - reigns over tools available on network.
- Session - manages how data is saved, feels a bit redundant. Needs far more investigation.
- Human in the loop - allows humans control the agent runs to some extent
- Real time agents - seems reigns over stuff like voice input, somehow detects intreruptions.


## Meta

All the sections of tutorial and docs will be combined in section above. Definetly gonna go over tutorials and examples. Not sure about API, maybe too, or at least part of them.

Finished:
- Intro
- Quickstart
- Next: Configuration, finished reading, applying configurations to simple example. So finish those then make define actors and their domains.
