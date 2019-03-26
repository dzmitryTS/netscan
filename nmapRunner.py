import nmap
import json
import datetime

DEFAULT_IPS = './results/ips.txt'

DEFAULT_OPTIONS = [
    '-iL ./results/ips.txt -F -host-timeout',
    '-iL ./results/ips.txt -sV -host-timeout',
    '-iL ./results/ips.txt -sN -host-timeout',
    '-iL ./results/ips.txt -sN -O -host-timeout',
    '-iL ./results/ips.txt -A -host-timeout',
    '-iL ./results/ips.txt -sV -D -f -host-timeout',
    '-iL ./results/ips.txt -sP -host-timeout',
]

#not used yet
class NmapScanner():
    #gets optional wait time for each host in minutes and
    #optional path to text file with options ofr nmap command(except for waittime)
    def __init__(self, waitTime = 2, optionsPath = None, ):
        self.nm = nmap.PortScanner()

        if (optionsPath == None):
            self.options = DEFAULT_OPTIONS
        else:
            self.options = self._getOptions(optionsPath)
        
        self.waitTime = waitTime


    #retrives options from file provided in <path>
    def _getOptions(self, path):
        options = []
        with open(path, 'r') as f:
            for option in f:
                options.append(option)
        
        return options

    #performes single scan with <parameters> and
    #writes result in file by <path> address
    def scan(self, parameters, path):
        parameters = parameters+ ' {}m'.format(self.waitTime)
        print(str(datetime.datetime.now()) + ' Nmap: performing scan for ' + parameters)

        result = self.nm.scan(arguments=parameters)
        with open(path, 'w') as f:
            f.write(json.dumps(result['scan']))

        print(str(datetime.datetime.now()) + ' Nmap: scan ended')

    #performes single scan for each option in self.options
    def scanAll(self):
        for i in range (len(self.options)-1):       
            resultPath = './results/result_' + str(i)
            self.scan(self.options[i], resultPath)


