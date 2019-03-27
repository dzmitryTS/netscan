import plac
import subprocess

def main(mac, mask):
    print('ok')

def resolveIP(mac, mask):
    s = subprocess.check_output(['netdiscover', mask, '-P'])
    print(s)

if __name__ == "__main__":
    plac.call(main)