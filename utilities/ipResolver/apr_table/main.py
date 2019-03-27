import plac
from python_arptable import get_arp_table
import json


def main(mac):
    result = resolveIPbyMAC(mac)
    print(result)


def resolveIPbyMAC(mac):
    hosts = json.dumps(get_arp_table())
    for host in hosts:
        if host['HW address'] == mac:
            return host['IP address']

if __name__ == '__main__':
    plac.call(main)