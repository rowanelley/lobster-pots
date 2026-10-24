import os, time

def printLine(input, delay):
    time.sleep(delay)
    print(input)

def printChars(text, delay):
    for char in text:
        time.sleep(delay)
        print(char, end="")

def clear():
    os.system("cls" if os.name == "nt" else "clear")