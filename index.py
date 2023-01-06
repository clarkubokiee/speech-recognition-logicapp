import os
import azure.cognitiveservices.speech as speechsdk
import requests
import webbrowser
import time
#import array as arr

#This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
speech_config.speech_recognition_language="en-US"

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
print("Getting Access Token")
auth_response_json = auth_response.json()

status_code = auth_response.status_code
time.sleep(2)
print("The status code : " + str(status_code))
#"Bearer %s" %
auth_token = auth_response_json["access_token"]
auth_token_header_value = auth_token
#auth_token_header = {"Authorization ": auth_token_header_value}

#Auth HeaderHeader
header = {
    'Authorization' : 'Bearer ' + auth_token_header_value
}

audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

#Get the mic input and turn it into text
print("--CHOICES --")
print("")
time.sleep(2)
print("1. Endpoint Analytics\n2. Secure Score\n3. Breach")
print("")
time.sleep(2)
print("Speak into your microphone.")
speech_recognition_result = speech_recognizer.recognize_once_async().get()
speech_list = ['Endpoint analytics.', 'Secure.', 'Breach.', 'Analytics.', 'Score.', 'Samanage.', 'Manage.', 'Run endpoint analytics.', 'Run samanage.', 'Run score.', 'Run secure score.']
text = speech_recognition_result.text

print("You said : " + text)

Speech_Recognized = speechsdk.ResultReason.RecognizedSpeech
#Speech_Synthesized = speechsdk.ResultReason.SynthesizingAudioCompleted


#Loop for detecting if recognized text is equal to some intent
while speech_recognition_result.reason == Speech_Recognized:
    for i in speech_list:
        if(text == speech_list[0] or text == speech_list[3] or text == speech_list[7]):
            print("Processing Endpoint Analytics Logic App...")
            #Run Endpoint Analytics Logic App
            endpoint_analytics_url = "https://management.azure.com/subscriptions/b555cfaa-9a6c-4595-9eae-b740c56ad891/resourceGroups/rg-rafi-cloudgovernance/providers/Microsoft.Logic/workflows/logic-rafi-endpointanalytics/triggers/Recurrence/run?api-version=2016-06-01"
            endpoint_analytics_run = requests.post(endpoint_analytics_url, headers=header)
            endpoint_analytics_portalurl = "https://portal.azure.com/#@rafi.ph/resource/subscriptions/b555cfaa-9a6c-4595-9eae-b740c56ad891/resourceGroups/rg-rafi-cloudgovernance/providers/Microsoft.Logic/workflows/logic-rafi-endpointanalytics/logicApp"
            speech_synthesis_result = speech_synthesizer.speak_text_async("You have chosen Endpoint Analytics Logic App. Wait for few a seconds. Processing Endpoint Analytics Post Request.").get()
            time.sleep(10)
            speech_synthesis_result = speech_synthesizer.speak_text_async("Redirecting you to the Logic App Portal Overview History. Thank you.").get()
            webbrowser.open(endpoint_analytics_portalurl)
            break
        elif(text == speech_list[1] or text == speech_list[4] or text == speech_list[9] or text == speech_list[10]):
            print("Processing Secure Score Logic App...")
            #Running Secure Score Logic App in Azure Portal
            securescore_url = "https://management.azure.com/subscriptions/b555cfaa-9a6c-4595-9eae-b740c56ad891/resourceGroups/rg-rafi-cloudgovernance/providers/Microsoft.Logic/workflows/logic-rafi-securescore/triggers/Recurrence/run?api-version=2016-06-01"
            securescore_run = requests.post(securescore_url, headers=header)
            securescore_portalurl = "https://portal.azure.com/#@rafi.ph/resource/subscriptions/b555cfaa-9a6c-4595-9eae-b740c56ad891/resourceGroups/rg-rafi-cloudgovernance/providers/Microsoft.Logic/workflows/logic-rafi-securescore/logicApp"
            speech_synthesis_result = speech_synthesizer.speak_text_async("You have chosen Secure Score Logic App. Wait for few seconds. Processing Post Request.").get()
            time.sleep(10)
            print("Redirecting you to Portal Overview History. Thank you.")
            speech_synthesis_result = speech_synthesizer.speak_text_async("Redirecting you to the Logic App Portal Overview History. Thank you.").get()
            webbrowser.open(securescore_portalurl)
            break
        elif(text == speech_list[2] or text == speech_list[5] or text == speech_list[6] or text == speech_list[8]):
            print("Processing Samanage SLA Breach Logic App..")
            #Run Samanage Breach Logic App
            samanagesla_url = "https://management.azure.com/subscriptions/b555cfaa-9a6c-4595-9eae-b740c56ad891/resourceGroups/rg-rafi-cloudgovernance/providers/Microsoft.Logic/workflows/logic-rafi-samanagesla/triggers/Recurrence/run?api-version=2016-06-01"
            samanagesla_run = requests.post(samanagesla_url, headers=header)
            samanagesla_portalurl = "https://portal.azure.com/#@rafi.ph/resource/subscriptions/b555cfaa-9a6c-4595-9eae-b740c56ad891/resourceGroups/rg-rafi-cloudgovernance/providers/Microsoft.Logic/workflows/logic-rafi-samanagesla/logicApp"
            speech_synthesis_result = speech_synthesizer.speak_text_async("You have chosen Samanage Breach Logic App. Please Wait for 1 to 2 minutes. Processing Post Request.").get()
            time.sleep(120)
            print("Redirecting you to Portal Overview History. Thank you.")
            speech_synthesis_result = speech_synthesizer.speak_text_async("Redirecting you to the Logic App Portal Overview History. Thank you.").get()
            webbrowser.open(samanagesla_portalurl)
        else:   
            print("Oh no! No such keyword is recorded in my personal paking bobo na mind.")
            speech_synthesis_result = speech_synthesizer.speak_text_async("Oh no! No such keyword is recorded in my personal bobo na mind.").get()
            break
    break
#Loop For Checking If Recognized Speech is Cancelled            
while speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_recognition_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")






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


"""
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