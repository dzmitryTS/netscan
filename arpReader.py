from python_arptable import get_arp_table
import json

def resolveIPbyMAC(mac):
    hosts = json.loads(get_arp_table())
    for host in hosts:
        print(host)