"""Flask application for emotion detection."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """Render the homepage."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detection_route():
    """Handle emotion detection requests."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return {"message": "Invalid text! Please provide input text."}, 400

    result = emotion_detector(text_to_analyze)

    if not result or result.get("dominant_emotion") is None:
        return {"message": "Invalid text! Please try again!"}, 400

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"{result['dominant_emotion']}."
    )

    return {"response": response_text}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
