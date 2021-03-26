import os
from calculator import Callculator
import colored

def cleaning():
    os.system("cls")

print("  /$$$$$$   /$$$$$$        /$$    /$$  /$$$$$$ \n /$$__  $$ /$$__  $$      | $$   | $$ /$$__  $$\n| $$  \ $$| $$  \__/      | $$   | $$|__/  \ $$\n| $$  | $$|  $$$$$$       |  $$ / $$/  /$$$$$$/\n| $$  | $$ \____  $$       \  $$ $$/  /$$____/ \n| $$  | $$ /$$  \ $$        \  $$$/  | $$      \n|  $$$$$$/|  $$$$$$/         \  $//$$| $$$$$$$$\n \______/  \______/           \_/|__/|________/")

print("welcome, What whould you like to open?")
print("1.Calculater \n2.Diary \n3.webbrowser \n4.exit")
print(colored('hello', 'red'), colored('world', 'green'))
choose = int(input(">>> "))

#
#Call programs
#

if(choose == 1):
    cleaning()
    Callculator()
elif():
    cleaning()
