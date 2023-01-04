import os
import azure.cognitiveservices.speech as speechsdk
import requests
import webbrowser
#import array as arr

#This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
speech_config.speech_recognition_language="en-US"

"""
#Body Data for Getting Microsoft Graph API token
client_id = "08d838d3-df77-4ef4-8a1c-8097db057024"
client_secret = "CCs8Q~NJFJ.e5SDWsxJ1q2FHCZzDzBk74-nJ5cKn"
resource = "https://management.azure.com"
grant_type = "client_credentials"

token_data = {
    "grant_type": grant_type,
    "client_id": client_id,
    "client_secret": client_secret,
    "resource" : resource
}

#Get token value
get_token_url = "https://login.microsoftonline.com/4f2f5733-1a9d-48ac-98f4-a6c588424b7b/oauth2/token"

auth_response = requests.post(get_token_url, data=token_data)
auth_response_json = auth_response.json()

status_code = auth_response.status_code
print("The status code : " + str(status_code))
#"Bearer %s" %
auth_token = auth_response_json["access_token"]
auth_token_header_value = auth_token
#auth_token_header = {"Authorization ": auth_token_header_value}

#Auth HeaderHeader
header = {
    'Authorization' : 'Bearer ' + auth_token_header_value
}
#Run Endpoint Analytics Logic App
endpoint_analytics_url = "https://management.azure.com/subscriptions/b555cfaa-9a6c-4595-9eae-b740c56ad891/resourceGroups/rg-rafi-cloudgovernance/providers/Microsoft.Logic/workflows/logic-rafi-endpointanalytics/triggers/Recurrence/run?api-version=2016-06-01"
endpoint_analytics = requests.post(endpoint_analytics_url, headers=header)
#Run Secure Score Logic App
securescore_url = "https://management.azure.com/subscriptions/b555cfaa-9a6c-4595-9eae-b740c56ad891/resourceGroups/rg-rafi-cloudgovernance/providers/Microsoft.Logic/workflows/logic-rafi-securescore/triggers/Recurrence/run?api-version=2016-06-01"
securescore_run = requests.post(securescore_url, headers=header)
#Run Samanage SLA breaches Logic App
samanagesla_url = "https://management.azure.com/subscriptions/b555cfaa-9a6c-4595-9eae-b740c56ad891/resourceGroups/rg-rafi-cloudgovernance/providers/Microsoft.Logic/workflows/logic-rafi-samanagesla/triggers/Recurrence/run?api-version=2016-06-01"
samanagesla_run = request.post(samanagesla_url, headers=header)
"""

audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

#Get the mic input and turn it into text
print("Speak into your microphone.")
speech_recognition_result = speech_recognizer.recognize_once_async().get()
intent = [
    " Endpoint analytics", "Neil"
]
text = speech_recognition_result.text
print("You said : " + text)

Speech_Recognized = speechsdk.ResultReason.RecognizedSpeech
#Speech_Synthesized = speechsdk.ResultReason.SynthesizingAudioCompleted

"""
#Loop for detecting if recognized text is equal to some intent
while speech_recognition_result.reason == Speech_Recognized:
    for key in intent:
        if key == text:
            speech_synthesis_result = speech_synthesizer.speak_text_async("I am freaking dumb as f***.").get()
            break
"""
"""  
if speech_recognition_result.reason == Speech_Recognized:
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
    print("Speech synthesized for text [{}]".format(text))
elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_recognition_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
"""