import os
from flask import Flask, render_template, request, redirect
import google.generativeai as genai

# Secure API key
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

app = Flask(__name__)

def generate(youtube_link, model, additional_prompt):
    if not additional_prompt:
        additional_prompt = ""

    prompt = f"Please provide a detailed summary of this YouTube video:\n{youtube_link}\n\nAdditional instructions: {additional_prompt}"

    try:
        response = genai.GenerativeModel(model).generate_content(prompt)
        return response.text if response.text else "No summary generated"
    except Exception as e:
        return f"Error generating summary: {str(e)}"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    youtube_link = request.form.get('youtube_link', '')
    model = request.form.get('model', 'gemini-2.0-flash-001')
    additional_prompt = request.form.get('additional_prompt', '')

    summary = generate(youtube_link, model, additional_prompt)
    return summary

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
