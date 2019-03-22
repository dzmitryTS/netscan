import netaddr
import json

inputFile = './results/result_1.json'
outputFile = './results/ips.txt'

ips = []

def retriveIPs():
    with open(inputFile, newline='') as f:
        raw = f.read()
        data = json.loads(raw)
        for key in data.keys():
            ips.append(key)
    with open(outputFile, 'a+') as ff:
        for ip in ips:
            ff.write(ip + '\n')
    


