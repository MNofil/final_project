from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    # Get the text from query param ?text=...
    text_to_analyze = request.args.get("text")
    
    if not text_to_analyze:
        return "Error: No text provided", 400

    # Call your emotion detection function
    result = emotion_detector(text_to_analyze)

    if isinstance(result, dict) and "dominant_emotion" in result:
        # Format response as required
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return response_text
    else:
        return "Error: Invalid response from emotion detector", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
