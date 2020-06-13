#!/usr/bin/python

import os
import signal
from subprocess import Popen
import sys

import pyautogui
import random
import time

def randomPhrase(fileOfWords):
    listOfWords = []
    for word in fileOfWords:
        listOfWords.append(word.replace("\n", ""))

    lengthOfPhrase = random.randrange(5, 20)

    listLen = len(listOfWords)-1
    string = ""

    for i in range(0, lengthOfPhrase):
        pos = int(random.randrange(0, listLen))
        string = string + listOfWords[pos] + " "

    writeAndSendMessage(string)

def writeAndSendMessage(text):
    pyautogui.write(str(text), 0)#scrive(messaggio, tempo di digitazione delle lettere)
    pyautogui.press('enter')

def main():
    platform = sys.platform #get the system information

    print("Start, press enter to stop the process")

    if(platform == "linux" or platform == "linux2"): #for linux
        spamProcess = Popen("./spamFunction.py") #start the process

        input()

        os.kill(spamProcess.pid, signal.SIGKILL) #kill the process

    if(platform == "win32" or platform == "cygwin"): #for windows
        spamProcess = Popen("python spamFunction.py") #start the process

        input()

        os.kill(spamProcess.pid, signal.SIGTERM) #kill the process

    else:
        print("NOOOOOOO")


if __name__ == "__main__":
    main()