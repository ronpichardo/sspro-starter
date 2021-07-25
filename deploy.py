import requests
import os, sys, json

vc4_server = os.getenv('VC4_SERVER_URL')
vc4_api_key = os.getenv('VC4_API_KEY')

file_path = sys.argv[1]

headers = {
    'accept': 'application/json',
    'Authorization': vc4_api_key
}

form_data = {
    'ProgramId': 2,
    'FriendlyName': 'SSProJenkins',
    'Notes': 'Jenkins Deployed This',
    'StartNow': True
}

program_file = {
    'AppFile': open(file_path, 'rb')
}

deploy = requests.put(f'{vc4_server}/VirtualControl/config/api/ProgramLibrary', headers=headers, files=program_file, data=form_data)
print(deploy.content)