from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Create assistant and user agents
assistant = AssistantAgent(
    name="assistant",
    llm_config={
        "config_list": [{"model": "gpt-4", "api_key": "your-api-key"}],
        "temperature": 0.7,
    },
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
)

# Start a conversation
user_proxy.initiate_chat(
    assistant,
    message="What are the key features of Microsoft AutoGen?",
)
