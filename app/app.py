from flask import Flask, render_template, request
import pandas as pd
import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Load cleaned data
data = pd.read_csv('./data/cleaned_data.csv')

def query_chatgpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Replace with "gpt-4" if you have access
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,  # Adjust as needed
        temperature=0.7  # Adjust as needed
    )
    return response.choices[0].message['content'].strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    query = request.form['query']
    answer = query_chatgpt(query)
    return render_template('result.html', query=query, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
