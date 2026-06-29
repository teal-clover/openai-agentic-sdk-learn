# Agents

Mar 30 - New structure = for each chapter we can have only one code file, two hours for one chapter is the ideal limit, although increase in time is better than skimming.
Cannot fit all here, will have lots of "draft" data, which I don't want to lose. Gonna use google docs https://docs.google.com/document/d/15cvqaJuMKumK_P4M96GfhBA5H5XDB7kcr0XuCUDNumQ/edit?usp=sharing

## Quickstart

Actors and their domains

- Agents - the rulers of the agentic domain.
  - Agent loop - not sure if actor, or action that actor does.
  - Runner - has API page
    - Can use session
      - Can resuse *OPENAI server-managed state*. Idk what is that. (Running agents will explain.)
    - can override default configurations from Agents in it's own domain using `run_config=RunConfig(trace_include_sensitive_data=False)`
  - RunResult - same API page, gonna skip for tutorial time.
    - Can move response back to input list. Provides full controller to the runner over the text.
  - can directly change configuratoin throught helper methods in main packenge (agents), like `set_default_openai_key`, `set_tracing_disabled(True)` or through global env variables `expot OPENAI_AGENTS_TRACE_INCLUDE_SENSITIVE_DATA=0`
  - For Debugging: `enable_verbose_stdout_logging()` is used to simplify development, and we can even attach to the emited logs `logging.getLogger("openai.agents")`
    - `logging` library is the ruler there.
- Agent as tools and Handoffs
  - Agent as tools - orchestrator agent still decides what to do with data
  - Handoffs - full responsibility to other agent
- Guardrails
- Tracing - tracing and evaluation, thanks to OpenAI suite
- Tools - functions that have reign over the backend code, may be invoked by agents.
  - Pydantic schemas - provide tool the ability to define what will come in and out.
  - MCP - reigns over tools available on network.
  - You can say to agent if you want the tool to be the ending, no more processing (interesting if it is possible to do next to tool itself)
  - Or you can force its call.
- Session - manages how data is saved, feels a bit redundant. Needs far more investigation.
- Human in the loop - allows humans control the agent runs to some extent
- Real time agents - seems reigns over stuff like voice input, somehow detects intreruptions.
- Context - injected in each tool call, can be specified as a python object (I prefer pydantic models)
  - There are some serialization caveats.

## Questions

- Can handoffs be used inside tool agents?


## Meta

All the sections of tutorial and docs will be combined in section above. Definetly gonna go over tutorials and examples. Not sure about API, maybe too, or at least part of them.

Finished:
- Intro
- Quickstart
- Next: Configuration, finished reading, applying configurations to simple example. So finish those then make define actors and their domains.


## Further
- https://docs.python.org/3/howto/logging.html - Severe need to go thrught this.
