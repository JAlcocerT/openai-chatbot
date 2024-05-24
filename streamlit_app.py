import openai
import streamlit as st

with st.sidebar:
    st.title('🤖💬 OpenAI Chatbot')
    # if 'OPENAI_API_KEY' in st.secrets:
    #     st.success('API key already provided!', icon='✅')
    #     openai.api_key = st.secrets['OPENAI_API_KEY']
    # else:
    openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
    if not (openai.api_key.startswith('sk-') and len(openai.api_key)==51):
        st.warning('Please enter your credentials!', icon='⚠️')
    else:
        st.success('Proceed to entering your prompt message!', icon='👉')

    # Dropdown menu to select the model
    model_choice = st.selectbox(
        'Choose the model:',
        ['gpt-3.5-turbo', 'gpt-4-turbo-preview','gpt-4o'],
        index=0  # Default selection is gpt-3.5-turbo
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=model_choice,  # Use the selected model from the dropdown
            messages=[{"role": m["role"], "content": m["content"]}
                      for m in st.session_state.messages], stream=True):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
