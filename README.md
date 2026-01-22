<div align="center">
  <img src="logo.png" alt="sandbox-autogen" width="512"/>

  # sandbox-autogen

  [![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
  [![AutoGen](https://img.shields.io/badge/AutoGen-0.4-orange.svg)](https://microsoft.github.io/autogen/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  **A sandbox for experimenting with Microsoft AutoGen multi-agent conversations**

  [AutoGen Docs](https://microsoft.github.io/autogen/) · [AutoGen GitHub](https://github.com/microsoft/autogen)
</div>

## Overview

This sandbox provides ready-to-run examples for exploring Microsoft AutoGen - a framework for building LLM applications using multiple agents that converse to solve tasks. Includes examples for both legacy and modern async APIs.

## Features

- Single agent async example with OpenAI GPT-4o
- Multi-agent team with web browsing capabilities
- Round-robin group chat orchestration
- Environment-based API key management

## Quick Start

```bash
# Create and activate environment
conda env create -f environment.yml
conda activate autogen-sandbox

# Set up your OpenAI API key
cp .env.example .env
# Edit .env and add your key

# Run the simple agent example
python single.py
```

## Examples

| File | Description | API Style |
|------|-------------|-----------|
| `single.py` | Single agent "Hello World" | Modern async |
| `team.py` | Multi-agent team with web surfer | Modern async |
| `example.py` | Basic agent conversation | Legacy sync |

### Single Agent

```python
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

agent = AssistantAgent("assistant", OpenAIChatCompletionClient(model="gpt-4o"))
print(await agent.run(task="Say 'Hello World!'"))
```

### Multi-Agent Team

```python
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.agents.web_surfer import MultimodalWebSurfer

assistant = AssistantAgent("assistant", model_client)
web_surfer = MultimodalWebSurfer("web_surfer", model_client)
team = RoundRobinGroupChat([web_surfer, assistant, user_proxy])
```

## Project Structure

```
├── environment.yml    # Conda environment definition
├── .env.example       # Environment template
├── single.py          # Single agent example
├── team.py            # Multi-agent team example
└── example.py         # Legacy API example
```

## Dependencies

- `autogen-agentchat` - Core AutoGen framework
- `autogen-ext[openai,web-surfer]` - OpenAI and web browsing extensions
- `playwright` - Browser automation for web surfer
- `python-dotenv` - Environment variable management

## Resources

- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [AutoGen GitHub](https://github.com/microsoft/autogen)
- [AutoGen Studio](https://microsoft.github.io/autogen/docs/studio)

## License

MIT
