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
from data_scrapper import *
from langchain_openai import ChatOpenAI
llm=ChatOpenAI(api_key="",model="gpt-3.5-turbo")
# Load environment variables
load_dotenv()
#KEY = os.getenv("OPENAI_API_KEY")
#KEY=st.secrets["OPENAI_API_KEY"]

# Streamlit setup
st.write("Please enter the link below:")

# Text input for the Google Form link
user_link = st.chat_input("Paste your Google Form link here")

# Variable to store the result of the function
result = None

# Display the entered link and call a function on submission
if user_link:
    if st.button("Submit"):
        # Call the function to get Google Form questions and store the returned value in a variable
        result = get_google_form_questions(user_link)

# Check if the result is not None and proceed with extracting information
if result:
    system_msg_template = SystemMessagePromptTemplate.from_template(
        template="""Please extract the following information from the paragraph provided by the user and return only the key-value pairs. Do not include any other words or explanations."""
    )

    human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")

    prompt_template = ChatPromptTemplate.from_messages([system_msg_template, human_msg_template])

    conversation = ConversationChain(prompt=prompt_template, llm=llm)

    # Get user input for the paragraph containing the information
    para = st.chat_input("Enter all the information which you want to fill in the Google Form")

    if para:
        response = conversation.predict(input=f"Paragraph provided:\n{para}\n\nInformations to be extracted:\n{result}")
        st.write("Extracted Information (Key-Value Pairs):")
        st.json(response)