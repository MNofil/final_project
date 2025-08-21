import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Send POST request
    response = requests.post(url, headers=headers, json=input_json)
    
    if response.status_code != 200:
        return {"error": f"Request failed with status {response.status_code}"}
    
    # Convert JSON string to Python dict
    response_dict = json.loads(response.text)
    
    # Extract emotion scores
    emotions = response_dict["emotionPredictions"][0]["emotion"]
    
    anger = emotions.get("anger", 0)
    disgust = emotions.get("disgust", 0)
    fear = emotions.get("fear", 0)
    joy = emotions.get("joy", 0)
    sadness = emotions.get("sadness", 0)
    
    # Find dominant emotion
    emotion_scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return in required format
    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }
