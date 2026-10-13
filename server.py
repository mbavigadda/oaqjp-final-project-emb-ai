"""
Flask server for the Emotion Detection application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
 
app = Flask("Emotion Detector")
 
@app.route("/emotionDetector")
def emot_detector():
    """
    Receives text from the web page, runs emotion detection on it,
    and returns the formatted result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
 
    dominant_emotion = response['dominant_emotion']
 
    # Error handling: blank or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
 
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
 
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
 
@app.route("/")
def render_index_page():
    """
    Renders the main application page.
    """
    return render_template('index.html')
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)