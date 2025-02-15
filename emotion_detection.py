import requests
import json

def emotion_detector(text_to_analyze):
    """
    Function to detect emotions using Watson NLP EmotionPredict API.
    Returns a dictionary with emotion scores and the dominant emotion.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        # Convert the response JSON to a dictionary
        response_data = response.json()

        # Extract emotion scores
        emotions = response_data.get("emotionPredictions", [{}])[0].get("emotion", {})

        # Extract required emotions
        result = {
            "anger": emotions.get("anger", 0.0),
            "disgust": emotions.get("disgust", 0.0),
            "fear": emotions.get("fear", 0.0),
            "joy": emotions.get("joy", 0.0),
            "sadness": emotions.get("sadness", 0.0),
        }

        # Find the dominant emotion
        result["dominant_emotion"] = max(result, key=result.get)

        return result
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

# Testing the function
if __name__ == "__main__":
    test_text = "I am so happy I am doing this."
    print(emotion_detector(test_text))

