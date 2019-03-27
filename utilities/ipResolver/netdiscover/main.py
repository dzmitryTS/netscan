import plac
import subprocess

def main(mac, mask):
    resolveIP(mac, mask)

def resolveIP(mac, mask):
    s = subprocess.check_output(['netdiscover', '-r', mask, '-P'])
    print(s)

if __name__ == "__main__":
    plac.call(main)
