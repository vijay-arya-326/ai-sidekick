import os

keysRequired = [
    "SERPER_API_KEY",
    "GPT_MODEL",
    "OPENAI_API_KEY",
    "EMAIL_API_KEY",
    "DEFAULT_FROM_ADDRESS"
]

def validate_required_keys():
    missing_env = False
    for key in keysRequired:
        key_value = os.getenv(key) or None
        if key_value is None:
            print(f"Please set environment variable {key}")
            missing_env = True

    if missing_env:
        exit(1)
