import os, time

def printLine(text, delay):
    time.sleep(delay)
    print(text)

def printChars(text, delay):
    for char in text:
        time.sleep(delay)
        print(char, end="")

def clear():
    os.system("cls" if os.name == "nt" else "clear")