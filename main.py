from watson_developer_cloud import TextToSpeechV1
import json

text_to_speech = TextToSpeechV1(
    iam_apikey ='PU02inDLofPF8OBpiX8aAMVtnmukTUqyfvZbPJPu1U9z',
    url='https://gateway-wdc.watsonplatform.net/text-to-speech/api'
)

voices = text_to_speech.list_voices().get_result()
print(json.dumps(voices, indent=2))