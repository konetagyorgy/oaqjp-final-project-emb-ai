"""
Flask web application for detecting emotions in text input.

Provides an endpoint `/emotionDetector` that returns emotion scores
and the dominant emotion for a given sentence.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Receive text from the HTML interface and perform emotion analysis.

    Uses the `emotion_detector()` function to calculate scores for each emotion
    and determine the dominant emotion. Returns the results formatted for display.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please, try again!"
    return (
        f"For the given statement, the system response is: <br>"
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, 'sadness': {sadness}. <br>"
        f"The dominant emotion is: {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    '''Run the render_template function on the HTML template (index.html)
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
