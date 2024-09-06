import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Custom header specifying the model ID for the emotion analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Extracting the first item from the emotionPredictions list
    emotion_predictions = formatted_response.get('emotionPredictions', [{}])[0]
    
    # Extracting individual emotion scores from the 'emotion' dictionary
    emotions = emotion_predictions.get('emotion', {})
    anger = emotions.get('anger', 0)
    disgust = emotions.get('disgust', 0)
    fear = emotions.get('fear', 0)
    joy = emotions.get('joy', 0)
    sadness = emotions.get('sadness', 0)
    
    # Find the dominant emotion
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Returning a dictionary containing emotion analysis results and the dominant emotion
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }

