import requests

def emotion_detector(text_to_analyze):
    """
    Function to detect emotions using Watson NLP EmotionPredict API.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()  # Return the full response JSON
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

# Testing the function
if __name__ == "__main__":
    test_text = "I love this new technology."
    print(emotion_detector(test_text))
