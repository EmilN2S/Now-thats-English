from ollama import chat


def ask_model(user_text, model):
    messages = [
    {
        'role': 'user',
        'content': f'{user_text}',
    },
    ]

    response = chat(model, messages=messages)
    print(response['message']['content'])