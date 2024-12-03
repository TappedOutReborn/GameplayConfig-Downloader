import requests

from google.protobuf.json_format import MessageToJson
import TappedOut_pb2

headers = {
    'Accept': '*/*',
    'Content-Type': 'application/x-protobuf',
    'mh_client_version': 'Android.4.69.5',
    'client_version': '4.69.5',
    'server_api_version': '4.0.0',
    'EA-SELL-ID': '857120',
    'Connection': 'Keep-Alive',
    'platform': 'android',
    'os_version': '9.0.0',
    'hw_model_id': '0 0.0',
    'data_param_1': '1495502718',
}

print('[i] Making GameplayConfigResponse Object...')
gameplayConfigResponse = TappedOut_pb2.GameplayConfigResponse()

print('[i] Sending request...')
response = requests.get('https://prod.simpsons-ea.com/mh/gameplayconfig', headers=headers)

print('[i] Saving response...')
gameplayConfigResponse.ParseFromString(response.content)
with open('GameplayConfig.json', 'w') as outFile:
    outFile.write( MessageToJson(gameplayConfigResponse) )
    outFile.close()

print('[i] All done')
