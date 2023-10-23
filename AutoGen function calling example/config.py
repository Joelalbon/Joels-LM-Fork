import autogen

open_ai_config_list = autogen.config_list_from_json(
    "openai_key",
    filter_dict={
        "model": ["gpt-3.5-turbo"],
    },
)

coders = [{
    "api_type": "open_ai",
    "api_base": "http://192.168.123.34:1234/v1",
    "api_key": "NULL",
}]

assistants = [{
    "api_type": "open_ai",
    "api_base": "http://192.168.123.59:1234/v1",
    "api_key": "NULL",
}]
