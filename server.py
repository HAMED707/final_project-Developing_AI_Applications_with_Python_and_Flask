from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection_route():

    text_to_analyse = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyse)

    if result["dominant_emotion"] is None:
        return {"message": "Invalid text! Please try again!"}


    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
