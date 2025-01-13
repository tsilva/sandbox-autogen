# sandbox-autogen

A sandbox environment for experimenting with Microsoft AutoGen - a framework that enables development of LLM applications using multiple agents that can converse with each other to solve tasks.

## Prerequisites

- Python 3.10+
- Conda package manager
- OpenAI API key

## Setup

1. Create the conda environment:
```bash
conda env create -f environment.yml
```

2. Activate the environment:
```bash
conda activate autogen-sandbox
```

3. Create a `.env` file with your OpenAI API key:
```bash
echo "OPENAI_API_KEY=your-api-key" > .env
```

## Running Examples

1. Basic agent conversation:
```bash
python example.py
```

## Features Included

- Basic agent-to-agent conversation setup
- Integration with OpenAI models
- Web browsing capabilities with playwright
- AutoGen Studio support

## Project Structure

```
.
├── environment.yml    # Conda environment definition
├── example.py        # Basic example of agent interaction
└── .env              # Environment variables (create this)
```

## Resources

- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [AutoGen GitHub Repository](https://github.com/microsoft/autogen)
- [AutoGen Studio Documentation](https://microsoft.github.io/autogen/docs/studio)

## Notes

- Make sure to replace 'your-api-key' with your actual OpenAI API key
- The default example uses GPT-4. You can modify the model in example.py
- Web browsing features require playwright to be installed (included in environment.yml)
