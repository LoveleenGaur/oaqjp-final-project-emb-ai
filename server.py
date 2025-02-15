"""
Flask server for the Emotion Detection application.
Provides an API endpoint to analyze emotions in a given text.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    API endpoint to analyze emotions in a given text.
    Returns a formatted response including emotion scores and the dominant emotion.
    """
    data = request.get_json()
    
    if "text" not in data:
        return jsonify({"error": "Missing 'text' in request"}), 400

    text_to_analyze = data["text"]
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
