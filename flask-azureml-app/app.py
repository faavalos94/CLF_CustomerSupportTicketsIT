from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Load environment variable from .env
load_dotenv()

app = Flask(__name__)

# Get Azure ML details from environment
AZURE_ML_ENDPOINT = os.getenv('AZURE_ML_ENDPOINT')
AZURE_ML_API_KEY = os.getenv('AZURE_ML_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        # Get values from form
        text_input = request.form['text']
        len_words = request.form['len_words']

        # Construct the payload in the format required by Azure ML
        payload = {
            'input_data': {
                'columns': ['text', 'len_words'],
                'index': [1],
                'data': [
                    [text_input, int(len_words)]
                ]
            }
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {AZURE_ML_API_KEY}'
        }

        try:
            response = requests.post(AZURE_ML_ENDPOINT, json=payload, headers=headers)
            response.raise_for_status()
            prediction = response.json()
        except requests.exceptions.RequestException as e:
            prediction = f'Error: {str(e)}'

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)