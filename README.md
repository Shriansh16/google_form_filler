Deployed Link: https://appformfiller.streamlit.app/

Google Form Information Extractor
This project demonstrates how to automatically extract and fill information in Google Forms using a combination of web scraping and AI-powered text analysis. The application retrieves Google Form questions and provides a user interface for automatically extracting relevant information from user input. The extracted information can be used to fill out the form based on a paragraph provided by the user.

Features
Retrieve Google Form Questions: Automatically scrapes questions from a Google Form based on a user-provided link.
User Input Processing: Allows the user to input a paragraph of information.
AI-powered Information Extraction: Extracts key-value pairs from the user's paragraph using OpenAI's GPT-3.5 Turbo model.
Streamlit-based Interface: Provides an intuitive web interface for users to input the form link and their data.
Tech Stack
Python: Core language used to implement the scraping and data processing logic.
Streamlit: Used to create an interactive, easy-to-use web interface.
BeautifulSoup: Used for web scraping to extract form questions from the provided Google Form link.
OpenAI API: Used to extract key-value pairs from a user-provided paragraph using the GPT-3.5 Turbo model.

Future Enhancements
I am currently planning to extend this project by integrating CrewaAI to build a custom AI agent. This agent will:

Dynamically Fill Google Forms: The AI agent will automatically input extracted information into the appropriate fields of the Google Form, based on the form's structure.
Custom AI Agent Development: As CrewaAI does not have a predefined agent for this task, I will develop a custom AI agent specifically tailored to handle dynamic form navigation and input.

How to run?
1. Create a virtual environment using the command
"conda create -p venv python==3.10 -y"
2. Activate the environment using the command 
"conda activate venv"
3. Create a "secrets.toml" file in the project root directory and write this line:            
OPENAI_API_KEY = "your_openai_api_key_here"
4. Install all the dependencies using the command 
"pip install -r requirements.txt"
5. Execute "app1.py" using the command 
"streamlit run app1.py”
