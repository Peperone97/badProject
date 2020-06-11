#!/usr/bin/python

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
    print(string)
    writeAndSendMessage(string)

def sendworldByWorldAFile(file):
    # send messages
    for line in file:
        line = line.replace("\n", "")
        splittedLine = line.split(" ")
        print(splittedLine)
        for msg in splittedLine:
            writeAndSendMessage(msg)
            time.sleep(2)#delay tra un messaggio e l'altro

def writeAndSendMessage(text):
    pyautogui.write(str(text), 0.25)#scrive(messaggio, tempo di digitazione delle lettere)
    pyautogui.press('enter')

def main():
    file = open("fileToSend", "r")
    #file = open("paroleitaliane/1000_parole_italiane_comuni.txt", "r")

    #get mouse position
    x, y = pyautogui.position()
    pyautogui.click(x, y)

    sendworldByWorldAFile(file)
    #randomPhrase(file)

    file.close()

if __name__ == "__main__":
    main()