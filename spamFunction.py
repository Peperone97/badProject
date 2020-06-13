import pyautogui
import time
import signal
import sys

def signal_term_handler(signal, frame):
    print("Terminated")
    sys.exit(0)

def writeAndSendMessage(text):
    pyautogui.write(str(text), 0.25)# write(message, time of typing)
    pyautogui.press('enter')

def sendwordByWordAFile(file):
    # send messages
    for line in file: #get line by line
        line = line.replace("\n", "") #delete the new line character
        splittedLine = line.split(" ") #create a list of words
        print(splittedLine)
        for msg in splittedLine: #get word by word from list
            writeAndSendMessage(msg) #send the word
            time.sleep(2) #delay from one message a another

def main():
    file = open("fileToSend", "r") #open file of spam

    signal.signal(signal.SIGTERM, signal_term_handler)

    # get mouse position
    x, y = pyautogui.position()
    pyautogui.click(x, y)  # focus on the chat

    sendwordByWordAFile(file)

    file.close()

if __name__ == "__main__":
    main()