from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)  # Allow frontend to access this API

# Set your API key (better from environment variable)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY"))

@app.route("/generate-excuse", methods=["GET"])
def generate_excuse():
    lang = request.args.get("lang", "en")
    
    prompt = (
        "Give me a funny excuse in Malayalam for not doing homework"
        if lang == "ml"
        else "Give me a funny excuse in English for not doing homework"
    )
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        excuse = response.choices[0].message.content.strip()
        return jsonify({"excuse": excuse})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
