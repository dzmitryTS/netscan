from python_arptable import get_arp_table

def resolveIPbyMAC(mac):
    arp = get_arp_table()
    print(arp)