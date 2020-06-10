#!/usr/bin/python

import pyautogui
import time

def writeAndSendMessage(text):
    pyautogui.write(str(text))
    pyautogui.press('enter')

def main():
    file = open("fileToSend", "r")

    #get mouse position
    x, y = pyautogui.position()
    pyautogui.click(x, y)

    #send messages
    for line in file:
        line = line.replace("\n", "")
        splittedLine = line.split(" ")
        print(splittedLine)
        for msg in splittedLine:
            writeAndSendMessage(msg)
            time.sleep(0.5)

    file.close()

if __name__ == "__main__":
    main()