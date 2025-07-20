from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from model import generate_answer

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "No question provided"}), 400
    answer = generate_answer(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
