#!/usr/bin/python

from subprocess import Popen
import sys

def main():

    platform = sys.platform #get the system information

    print("Start, press enter to stop the process")

    spamProcess = Popen(["python", "spamFunction.py"]) #start the process

    input()

    spamProcess.terminate()

    print(spamProcess.poll())

if __name__ == "__main__":
    main()