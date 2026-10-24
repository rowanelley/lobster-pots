import os, magicPrint as mp, time

def newSave():

    saveName = input("Name your save: ")

    mp.clear()
    time.sleep(1)
    mp.printChars("Statement of death for:\n", 0.1)
    time.sleep(0.5)
    mp.printChars("Mrs. P Player -\n", 0.1)
    time.sleep(0.5)
    mp.printChars("Grandmother of ", 0.1)
    playerName = input()
    mp.clear()

    while True:
        print('Your name is ' + playerName + '?')
        answer = input("Y/n: ").lower()
        if answer != 'n':
            break
        playerName = input("What shall we call you?")

    mp.clear()
    
    time.sleep(1)
    mp.printChars("Letter to "+ playerName + ',\n', 0.1)
    time.sleep(0.5)
    pots = 5
    mp.printChars("Your Grandmother has left you " + str(pots) + ' lobster pots.\n', 0.05)
    time.sleep(0.5)
    mp.printChars("She hopes you find a good use for them.", 0.05)