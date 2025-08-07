import requests

def chat_with_model(prompt):
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': 'mistral',
            'prompt': prompt,
            'stream': False
        }
    )
    return response.json()["response"]

if __name__ == "__main__":
    print("🤖 Mini ChatGPT (Mistral via Ollama)")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        reply = chat_with_model(user_input)
        print(f"Mistral: {reply}\n")
