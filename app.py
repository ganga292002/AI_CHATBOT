import streamlit as st
from google import genai

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

st.title("🤖 My AI Chatbot")

# Create chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input at the bottom
prompt = st.chat_input("Type your message...")

if prompt:

    # Show user message
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Ask Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    answer = response.text

    # Show AI response
    st.chat_message("assistant").markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
