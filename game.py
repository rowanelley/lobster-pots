import magicPrint as mp, time

mp.clear()

mp.printLine ("--------------", 0.7)
mp.printLine(" Lobster Pots", 0.7)
mp.printLine ("--------------", 0.7)
mp.printLine("", 0.7)
time.sleep(0.7)

mp.printChars("load or new: ", 0.1)
answer = input()
while True:
    if answer.lower() == "load" or answer.lower() == "new":
        break
    answer = input("load or new: ")