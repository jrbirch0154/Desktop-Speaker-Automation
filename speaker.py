# Speaker Starting
# Sat May 9 2026
# Jacob Birch

import requests
import sys
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('token')
wlc = os.getenv('wlc') # Laptop Charger
sp = os.getenv('sp') # Smart Plug
rsp = os.getenv('rsp') # Right Speaker
lsp = os.getenv('lsp') # Left Speaker
sub = os.getenv('sub') # Subwoofer
mon = os.getenv('mon') # Monitor
usb = os.getenv('usb') # USB Hub

HEADERS = {'Authorization':  f'Bearer {token}'}


# =============================================================================
# # GET DEVICE NAMES
# 
# URL = 'https://api.smartthings.com/v1/devices/'
# 
# response = requests.get(URL,headers=HEADERS)
# 
# data = response.json()
# 
# for device in data['items']:
#     print(device['deviceId'], device['label'])
# =============================================================================

devices = {
    'work laptop charger': wlc,
    'Smart Plug': sp,
    'RSpeaker': rsp,
    'LSpeaker': lsp,
    'Subwoofer': sub,
    'Monitor': mon,
    'USB Hub': usb  
    }

on = '{"commands":[{"component":"main","capability":"switch","command":"on"}]}'
off = '{"commands":[{"component":"main","capability":"switch","command":"off"}]}'

speakers = [devices['RSpeaker'],devices['LSpeaker'],devices['Subwoofer']]

URL = []
for numb in speakers:
    URL.append(f'https://api.smartthings.com/v1/devices/{numb}/commands')
    
    
def speakers(body,header=HEADERS,URL=URL):
    for url in URL:
        requests.post(url,headers=HEADERS,data=body)
        
        
if __name__ == '__main__':
        
    if sys.argv[1] == 'on':
        speakers(on)
    elif sys.argv[1] == 'off':
        speakers(off)
    else:
        print(f'Invalid input: {sys.argv[1]}.')