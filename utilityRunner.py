import json
import nmapRunner
import ipRetriever
import subprocess


BASE_COMMAND = '-iR 30 -A -f -host-timeout'
BASE_RESULT = './results/result_base.json'
IPS_FILE = './results/ips.txt'

def main(): 
    nm = nmapRunner.NmapScanner()
    nm.scan(BASE_COMMAND, BASE_RESULT)
    ipRetriever.retriveIPs(BASE_RESULT, IPS_FILE)

    nm.scanAll()


    

main()