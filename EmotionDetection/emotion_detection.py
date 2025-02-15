import requests
import json

def emotion_detector(text_to_analyze):
    """
    Function to detect emotions using Watson NLP EmotionPredict API.
    Handles empty text by returning None for all emotions.
    """
    if not text_to_analyze.strip():  # Check for empty input
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 400:  # Handle bad request response
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    if response.status_code == 200:
        response_data = response.json()
        emotions = response_data.get("emotionPredictions", [{}])[0].get("emotion", {})

        result = {
            "anger": emotions.get("anger", 0.0),
            "disgust": emotions.get("disgust", 0.0),
            "fear": emotions.get("fear", 0.0),
            "joy": emotions.get("joy", 0.0),
            "sadness": emotions.get("sadness", 0.0),
        }

        result["dominant_emotion"] = max(result, key=result.get) if any(result.values()) else None

        return result
    else:
        return {"error": f"Request failed with status code {response.status_code}"}
