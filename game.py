import magicPrint as mp, time, os, functions as f

try:
    os.mkdir("saves")
except:
    pass


mp.clear()

mp.printLine ("--------------", 0.5)
mp.printLine(" Lobster Pots", 0.5)
mp.printLine ("--------------", 0.5)
mp.printLine("", 0.5)
time.sleep(0.5)

mp.printChars("Welcome!", 0.1)
time.sleep(0.5)
print()
time.sleep(0.5)
print()
time.sleep(0.5)

saveDir = os.listdir('saves')

if len(saveDir) != 0:
    mp.printChars("Current saves are:\n", 0.1)
    time.sleep(0.5)
    for i in range(len(saveDir)):
        mp.printChars(str(i+1) + ') ' + saveDir[i], 0.1)
        time.sleep(0.5)
        print()
        time.sleep(0.5)
    print()
    time.sleep(0.5)
    mp.printChars("Enter save number to load,\n", 0.1)
    time.sleep(0.5)
    mp.printChars("or type \"new\": ", 0.1)
    input()