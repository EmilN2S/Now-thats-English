from ollama import chat


def ask_model(user_text, model) -> str:
    messages = [
    {
        'role': 'user',
        'content': user_text,
    },
    ]

    response = chat(model, messages=messages)
    return response['message']['content']