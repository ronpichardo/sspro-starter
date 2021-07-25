import requests
import os, sys

vc_server = os.getenv('VC4_SERVER_URL')
vc4_api_key = os.getenv('VC4_API_KEY')

headers = {
    'accept': 'application/json',
    'Authorization': vc4_api_key
}

deploy = requests.get(f'/VirtualControl/config/api/ProgramLibrary', headers=headers)

print(deploy.content)
