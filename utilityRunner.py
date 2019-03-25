import nmap
import json
import ipRetriever
import subprocess


BASE_COMMAND = '-iR 30 -A -f -host-timeout 2m'
BASE_RESULT = './results/result_base.json'
IPS_FILE = './results/ips.txt'
WAIT_TIME = 2

nmapOptions = [
    '-iL ./results/ips.txt -F -host-timeout',
    '-iL ./results/ips.txt -sV -host-timeout',
    '-iL ./results/ips.txt -sN -host-timeout',
    '-iL ./results/ips.txt -sN -O -host-timeout',
    '-iL ./results/ips.txt -A -host-timeout',
    '-iL ./results/ips.txt -sV -D -f -host-timeout',
    '-iL ./results/ips.txt -sP -host-timeout',
]

nm = nmap.PortScanner()

def scan(parameters, path):

    result = nm.scan(arguments=parameters)
    print(result)
    with open(path, 'w') as f:
        f.write(json.dumps(result['scan']))

def main():   
    scan(BASE_COMMAND, BASE_RESULT)
    ipRetriever.retriveIPs(BASE_RESULT, IPS_FILE)

    for i in range (len(nmapOptions)-1):       
        resultPath = 'result_{i}'
        scan(nmapOptions[i], resultPath)

#     ips = ipRetriever.convertIPs(IPS_FILE)
#     for ip in ips:
#         subprocess.run('nbtscan', '{netaddr.} -v -O ./results/nbtscan.json')


    

main()