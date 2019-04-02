import requests
import json

BASE_URL = "api.meraki.com/api/v0/"
ORGANIZATION = "840328"
NETWORK = "N_645140646620842548"
KEY = "c586ef3c82c83488579ec143ce7f146ce2429673"

def getData(MAC):
    url = 'organizations/{}/networks/{}/clients/{}'.format(ORGANIZATION, NETWORK, MAC)
    return _sendRequest(url)

def getAll():
    url = 'organizations/{}/networks/{}/devices/'.format(ORGANIZATION, NETWORK)
    devicesRaw = _sendRequest(url)
    devices = json.loads(devicesRaw.text)

    clients = []
    for device in devices:
        url = 'devices/{}/clients?timespan=86400'.format(device["serial"])
        currentClients = json.loads(_sendRequest(url))
        clients += currentClients

    return clients
    

def _sendRequest(requestURL):
    url = BASE_URL + requestURL
    headers = {
    'X-Cisco-Meraki-API-Key': KEY
    }
    response = requests.request('GET', url, headers = headers)
    #TODO non 200 handling
    return response.text