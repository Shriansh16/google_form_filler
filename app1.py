import os
import streamlit as st
from data_scrapper import get_google_form_questions
from openai import OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def get_response(input):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": input}] ,
    max_tokens=150,
    n=1
    )
    return response.choices[0].message.content
# Streamlit setup
st.write("Please enter the link below:")

# Text input for the Google Form link
user_link = st.text_input("Paste your Google Form link here")

# Check if the link is provided
result=None
if user_link:

        try:
            # Call the function to get Google Form questions and store the returned value
            result = get_google_form_questions(user_link)
            if result:
                st.write("Google Form Questions:")
                st.write(result)
            else:
                st.write("Failed to retrieve questions from the Google Form. Please check the link and try again.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Check if the result is available for extraction
para = st.text_area("Enter all the information which you want to fill in the Google Form")
submit1 = st.button("Submit",key="12")
if submit1:
        prompt = (
                f"Please extract the following information from the paragraph provided by the user and return only the key-value pairs. "
                f"Do not include any other words or explanations.\n\n"
                f"Paragraph provided:\n{para}\n\n"
                f"Informations to be extracted:\n{result}"
            )
        #input_prompt = prompt.format(para=para, result=result)
        st.write(prompt)
        #st.write("Extracted Information (Key-Value Pairs):")
        response = get_response(prompt)
        st.write(response)
        
            
