import streamlit as st
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
    return response.json().get("response", "No response")

st.title("Mini🤖SidGPT")

if "messages" not in st.session_state:
    st.session_state.messages = []

def add_message(user_input):
    reply = chat_with_model(user_input)
    st.session_state.messages.append({"user": user_input, "bot": reply})

user_input = st.text_input("Type your message:")

if user_input:
    add_message(user_input)
    # Clear the input box by resetting the session state key
    st.session_state["text_input"] = ""

for msg in st.session_state.messages:
    st.markdown(f"**You:** {msg['user']}")
    st.markdown(f"**Mistral:** {msg['bot']}")
