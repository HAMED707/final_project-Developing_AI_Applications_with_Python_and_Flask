import requests
import json

def emotion_detector(text_to_analyse):
    None_case={
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    if not text_to_analyse:
        return None_case

    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    myobj = { "raw_document": { "text": text_to_analyse } }

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        return None_case

    format_json=response.json()

    res= format_json["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(res, key=res.get)


    ans = {
        "anger": res["anger"],
        "disgust": res["disgust"],
        "fear": res["fear"],
        "joy": res["joy"],
        "sadness": res["sadness"],
        "dominant_emotion": dominant_emotion
    }

    
    print(ans)
    return ans