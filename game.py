import magicPrint as mp, time, os, functions as f

try:
    os.mkdir("saves")
except:
    pass


mp.clear()

mp.printLine ("--------------", 0.7)
mp.printLine(" Lobster Pots", 0.7)
mp.printLine ("--------------", 0.7)
mp.printLine("", 0.7)
time.sleep(0.7)

mp.printChars("Welcome! ", 0.1)
time.sleep(0.3)
mp.printChars("load save, or new save? ", 0.1)
answer = input()
while True:
    if answer.lower() == "load" or answer.lower() == "new":
        break
    answer = input("load or new? ")

if answer == 'new':
    f.newSave()