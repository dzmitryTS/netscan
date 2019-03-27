import subprocess

def scan(parameters, resultPath):
    subprocess.run(['nbtscan', parameters])
