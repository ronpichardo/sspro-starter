import requests
import os, sys

print(os.getenv('VC4_SERVER_URL'))

deploy = requests.get('http://192.168.30.93/VirtualControl/config/settings')
print(deploy.status_code)
