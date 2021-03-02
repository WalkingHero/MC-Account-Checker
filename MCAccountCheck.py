import requests
import json
import base64

username = input('Type the minecraft username you wish to look up: ')

response = requests.get("https://api.mojang.com/users/profiles/minecraft/"+ username)
x = response.json()
userid = x["id"]
name = x["name"]

response2 = requests.get("https://sessionserver.mojang.com/session/minecraft/profile/"+userid)
y = response2.json()['properties']
p = []

for d in y:
    val = d['value']
    p.append(val)

base64_message = p[0]
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

split = message.split('"')
skin = split[17]

print('ID:',userid)
print('Username:',name)
print('Skin URL:',skin)
if len(split) == 19:
    print('Cape: False')
elif len(split) > 19:
    print('Cape: True')

input('Press enter to exit...')