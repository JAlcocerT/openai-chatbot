* Prepare your environment:

```sh
git clone https://github.com/JAlcocerT/openai-chatbot

python -m venv openaichatbot #create it

openaichatbot\Scripts\activate #activate venv (windows)
source openaichatbot/bin/activate #(linux)

#deactivate #when you are done
```

* Run the App:

```sh
#pip install -r requirements.txt #all at once
streamlit run streamlit_app.py
```

* Use your OpenAI API: https://platform.openai.com/docs/models/continuous-model-upgrades

> Forked from [this project](https://github.com/dataprofessor/openai-chatbot)
---

# 🤖💬 OpenAI Chatbot

A conversational chatbot built in Python using Streamlit and the OpenAI LLM model GPT 3.5.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://openai-chatbot.streamlit.app/)

## Prerequisite libraries

```
streamlit
openai
```

## Get an OpenAI API key

You can get your own OpenAI API key by following the following instructions:
1. Go to https://platform.openai.com/account/api-keys.
2. Click on the `+ Create new secret key` button.
3. Next, enter an identifier name (optional) and click on the `Create secret key` button.

## Further Reading

- 🛠️ [Streamlit Documentation Tutorial on _**Build conversational apps**_](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps)
- 📖 [Streamlit Documentation on _**Chat elements**_](https://docs.streamlit.io/library/api-reference/chat)
