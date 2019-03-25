import netaddr
import json

ips = []

def retriveIPs(inputFile, outputFile):
    with open(inputFile, newline='') as f:
        raw = f.read()
        data = json.loads(raw)
        for key in data.keys():
            ips.append(key)
    with open(outputFile, 'a+') as ff:
        for ip in ips:
            ff.write('{ip}\n')

def convertIPs(inputFile):
    ips = []
    with open(inputFile, 'r') as f:
        for ip in f:
            ips.append(netaddr.IPAddress(ip))
    
    return ips

    


