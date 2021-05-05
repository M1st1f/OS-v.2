import os
from calculator import Callculator
from Diary import diary_entry

def cleaning():
    os.system("cls")

print("  /$$$$$$   /$$$$$$        /$$    /$$  /$$$$$$ \n /$$__  $$ /$$__  $$      | $$   | $$ /$$__  $$\n| $$  \ $$| $$  \__/      | $$   | $$|__/  \ $$\n| $$  | $$|  $$$$$$       |  $$ / $$/  /$$$$$$/\n| $$  | $$ \____  $$       \  $$ $$/  /$$____/ \n| $$  | $$ /$$  \ $$        \  $$$/  | $$      \n|  $$$$$$/|  $$$$$$/         \  $//$$| $$$$$$$$\n \______/  \______/           \_/|__/|________/")

print("welcome, What whould you like to open?")
print("1.Calculater \n2.Diary \n3.webbrowser \n4.exit")

choose = int(input(">>> "))

#
#Call programs
#
def infinty_util_death():
    while True:
        # TODO: loop program util choose is == 4
        #Problems? : loop kinda working, what I am doing worng??
        if(choose == 1):
            cleaning()
            Callculator()
            return True
            # TODO: how do I call back?
        elif(choose == 2):
            # TODO: Create a freaking Diary, How?
            cleaning()
            diary_entry()
            return True
        elif(choose == 3):
            ## TODO: Had already make this, just copy and paste
            cleaning()
            infinty_util_death()
            return True
        elif(choose == 4):
            return False
            SystemExit
        else:
            print("invalid text")
            infinty_util_death()
            return True

infinty_util_death()
