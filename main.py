#!/usr/bin/python

import pyautogui
import time


def fileToSend(fileName):
    file = open(fileName, "r")
    return file

def writeAndSendMessage(text, x, y):
    pyautogui.click(x-100, y)
    pyautogui.write(str(text))
    pyautogui.click(x, y)

def main():
    file = open("fileToSend", "r")

    #get mouse position
    x, y = pyautogui.position()
    print(str(x) + " " + str(y))

    #send messages
    for line in file:
        line = line.replace("\n", "")
        splittedLine = line.split(" ")
        print(splittedLine)
        for msg in splittedLine:
            writeAndSendMessage(msg, x, y)
            time.sleep(0.5)

    file.close()

if __name__ == "__main__":
    main()