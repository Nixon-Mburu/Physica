import json
from llamaapi import LlamaAPI
from flask import Flask, request, jsonify, render_template

llama = LlamaAPI("LA-bd7b0293eac14554aefba09a164b5d8c122c799df15d4d08b0a9b5c35f2ee73c")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('front.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    user_question = data.get('question', '')

    api_request_json = {
        "model": "llama3.1-70b",
        "messages": [
            {"role": "user", "content": user_question}
        ],
        "stream": False
    }

    response = llama.run(api_request_json)
    answer = response.json().get('choices', [{}])[0].get('message', {}).get('content', '')

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
