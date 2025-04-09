from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Lấy key từ biến môi trường

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Missing message"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render sẽ set PORT này
    app.run(host='0.0.0.0', port=port)

