from python_arptable import get_arp_table
import json

def resolveIPbyMAC(mac):
    hosts = json.dumps(get_arp_table())
    for host in hosts:
        print(host)

def testARP():
    hosts = get_arp_table()
    print(hosts[0])

testARP()