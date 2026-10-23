import os, time

def slowPrint(list, waitTime):
    text = ""
    for string in list:
        for char in string:
            text = text + char
            print(text)
            time.sleep(waitTime)
            os.system("clear")
        input(text)
        text = text + "\n"