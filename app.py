from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)  # allow requests from any origin

genai.configure(api_key="api key")
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/generate-excuse", methods=["GET", "POST"])
def generate_excuse():
    try:
        if request.method == "POST":
            data = request.get_json()
            reason = data.get("reason", "homework") if data else "homework"
            lang = data.get("lang", "ml") if data else "ml"
        else:
            reason = request.args.get("reason", "homework")
            lang = request.args.get("lang", "ml")

        # Generate prompt based on language
        if lang == "ml":
            prompt = f"{reason} ചെയ്യാത്തതിന് മലയാളത്തിൽ മാത്രം ഒരു ചെറിയ തമാശയുള്ള ഒഴികഴിവ് തരൂ "

        response = model.generate_content(prompt)
        excuse = response.text.strip()
        return jsonify({"excuse": excuse}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
