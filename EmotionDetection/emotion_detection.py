import requests  # Library for sending HTTP requests
import json      # Library for parsing JSON

def emotion_detector(text_to_analyze):
    # URL of the Watson NLP Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Header specifying the emotion model to use
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Input payload containing the text to analyze
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Send the POST request to the API
    response = requests.post(url, json=input_json, headers=headers)

    # 1. Convert the response text into a dictionary
    formatted_response = json.loads(response.text)

    # 2. Extract the required emotions and their scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # 3. Find the dominant emotion (the one with the highest score)
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # 4. Return the required output format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }