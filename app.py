import streamlit as st
import requests

st.title("🤝 Your Personal Assistant")

st.write("What can your personal assistant do?")

st.markdown("""
1. Answer questions on various topics.
2. Arrange calendar events and meetings.
3. Read and summarize emails.
4. Manage tasks and to-do lists.
5. Take quick notes.
6. Track expenses and budgeting.
""")

st.subheader("💬 Chat with your assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_message = st.chat_input("Your message")

if user_message:
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    with st.chat_message("user"):
        st.markdown(user_message)

    response = requests.post(
        "PASTE_YOUR_WEBHOOK_URL",
        json={"message": user_message}
    )

    if response.status_code == 200:
        result = response.json()
        assistant_message = result[0]["output"]

        st.session_state.messages.append({
            "role": "assistant",
            "content": assistant_message
        })

        with st.chat_message("assistant"):
            st.markdown(assistant_message)

    else:
        st.error(f"Error: {response.status_code}")
        st.write(response.text)
