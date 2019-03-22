import nmap
import json
import ipRetriever

nm = nmap.PortScanner()


def scan(parameters, path):

    result = nm.scan(arguments=parameters)
    print(result)
    with open(path, 'w') as f:
        f.write(json.dumps(result['scan']))

def main():   
    params = '-iR 100000 -A -f -host-timeout 20m'
    scan(params, './results/result_1.json')
    ipRetriever.retriveIPs()

    params = '-iL ./results/ips.txt -F -host-timeout 20m'
    scan(params, './results/result_2.json')

    params = '-iL ./results/ips.txt -sV -host-timeout 20m'
    scan(params, './results/result_3.json')

    params = '-iL ./results/ips.txt -sN -host-timeout 20m'
    scan(params, './results/result_4.json')

    params = '-iL ./results/ips.txt -sN -O -host-timeout 20m'
    scan(params, './results/result_5.json')

    params = '-iL ./results/ips.txt -sN -O -host-timeout 20m'
    scan(params, './results/result_5.json')

    params = '-iL ./results/ips.txt -A -host-timeout 20m'
    scan(params, './results/result_6.json')
    
    params = '-iL ./results/ips.txt -sV -D -f -host-timeout 20m'
    scan(params, './results/result_7.json')


main()