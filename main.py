#!/usr/bin/python

import os
import signal
from subprocess import Popen
import sys

def main():

    platform = sys.platform #get the system information

    print("Start, press enter to stop the process")

    spamProcess = Popen(["python", "spamFunction.py"]) #start the process

    input()

    os.kill(spamProcess.pid, signal.SIGTERM) #kill the process


if __name__ == "__main__":
    main()