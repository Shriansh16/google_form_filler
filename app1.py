import os
import streamlit as st
from dotenv import load_dotenv
from streamlit_chat import message
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
from data_scrapper import get_google_form_questions
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Securely retrieve the API key
#api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
llm = ChatOpenAI(api_key="", model="gpt-3.5-turbo")

# Streamlit setup
st.write("Please enter the link below:")

# Text input for the Google Form link
user_link = st.text_input("Paste your Google Form link here")

# Check if the link is provided
result=None
if user_link:
    if st.button("Submit"):
        try:
            # Call the function to get Google Form questions and store the returned value
            result = get_google_form_questions(user_link)
            if result:
                st.write("Google Form Questions:")
                st.json(result)
            else:
                st.write("Failed to retrieve questions from the Google Form. Please check the link and try again.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Check if the result is available for extraction
para = st.text_area("Enter all the information which you want to fill in the Google Form")

if para:
        try:
            prompt = (
                f"Please extract the following information from the paragraph provided by the user and return only the key-value pairs. "
                f"Do not include any other words or explanations.\n\n"
                f"Paragraph provided:\n{para}\n\n"
                f"Informations to be extracted:\n{result}"
            )
            st.write("Extracted Information (Key-Value Pairs):")
            response = llm(prompt)
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred during extraction: {e}")
