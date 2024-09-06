from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyzes the emotions of the provided text and returns a response string.

    Returns:
        str: A formatted string with emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Ensure that the text is provided
    if not text_to_analyze:
        return "Invalid text! Please try again!"

    # Call the emotion detector
    response = emotion_detector(text_to_analyze)

    # Extract individual emotion scores
    anger = response.get('anger', 0)
    disgust = response.get('disgust', 0)
    fear = response.get('fear', 0)
    joy = response.get('joy', 0)
    sadness = response.get('sadness', 0)
    dominant_emotion = response.get('dominant_emotion', 'unknown')

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Construct the response string
    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )
    
    return response_str

@app.route("/")
def render_index_page():
    """
    Renders the index page.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
