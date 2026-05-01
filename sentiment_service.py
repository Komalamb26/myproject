from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load sentiment model (runs once when server starts)
nlp = pipeline("sentiment-analysis")

# Test route (for browser check)
@app.route("/")
def home():
    return "Sentiment Analysis API is Running"

# Main API endpoint
@app.route("/analyze_sentiment", methods=["POST"])
def analyze_sentiment():
    try:
        data = request.get_json()

        # safety check
        if "text" not in data:
            return jsonify({"error": "No text provided"}), 400

        text = data["text"]

        # AI prediction
        result = nlp(text)[0]

        return jsonify({
            "text": text,
            "sentiment": result["label"],
            "confidence": float(result["score"])
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)