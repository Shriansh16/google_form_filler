import requests
from bs4 import BeautifulSoup

def get_google_form_questions(form_url):
    # Send a GET request to the Google Form URL
    response = requests.get(form_url)

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve the form.")
        return None

    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the form questions
    questions = []

    # Update the class name based on the form's HTML structure
    for question_block in soup.find_all('div', {'class': 'Qr7Oae'}):
        question_text = question_block.get_text(strip=True)
        questions.append(question_text)

    return questions


