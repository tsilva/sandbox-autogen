# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a sandbox environment for experimenting with Microsoft AutoGen - a framework for building LLM applications using multiple agents that converse to solve tasks. The project uses Python 3.10+ with Conda for environment management and OpenAI models for the agents.

## Environment Setup

1. Create and activate the conda environment:
```bash
conda env create -f environment.yml
conda activate autogen-sandbox
```

2. Set up environment variables:
```bash
# Copy the example and add your OpenAI API key
cp .env.example .env
```

## Running Examples

There are three example files demonstrating different AutoGen patterns:

- `python example.py` - Legacy example using older AutoGen API (note: uses hardcoded API key that should be replaced)
- `python single.py` - Simple single agent example using async API with dotenv
- `python team.py` - Multi-agent team with web surfing capabilities using RoundRobinGroupChat

## Architecture

### Agent Patterns

The project demonstrates two AutoGen API versions:

1. **Legacy API** (example.py): Uses `AssistantAgent` and `UserProxyAgent` with synchronous `initiate_chat()` pattern
2. **Modern Async API** (single.py, team.py): Uses async/await with:
   - `autogen_agentchat.agents` for agent classes
   - `autogen_ext.models.openai.OpenAIChatCompletionClient` for model clients
   - `RoundRobinGroupChat` for team coordination
   - `Console` UI for streaming output

### Key Components

- **Model Client**: `OpenAIChatCompletionClient` wraps OpenAI API calls (defaults to gpt-4o)
- **Agent Types**: `AssistantAgent` (AI-powered), `UserProxyAgent` (user interaction), `MultimodalWebSurfer` (web browsing)
- **Team Orchestration**: `RoundRobinGroupChat` manages turn-taking between agents
- **Termination**: `TextMentionTermination` allows graceful conversation ending

## Dependencies

Core packages (see environment.yml):
- `autogen-agentchat` - Main AutoGen framework
- `autogen-ext[openai,web-surfer]` - Extensions for OpenAI and web browsing
- `autogenstudio` - Visual interface for AutoGen (not used in examples)
- `playwright` - Browser automation for web surfing agent
- `python-dotenv` - Environment variable management

## Important Notes

- The README.md must be kept up to date with any significant project changes
- API keys should always be loaded from .env, never hardcoded (example.py violates this)
- Modern examples use async/await - prefer this pattern for new code
- Web surfing requires playwright installation and may need browser setup
