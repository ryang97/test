import requests
from requests.auth import HTTPDigestAuth
import json

url = "http://pokeapi.co/api/v2/pokemon/pikachu"

myResponse = requests.get(url, verify=True)

if(myResponse.ok):

    jData = json.loads(myResponse.content.decode("utf-8"))
    print(jData)
    
else:
    myResponse.raise_for_status()
