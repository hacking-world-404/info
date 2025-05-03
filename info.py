#------------- IMPORT ------------#
from os import system as c
import time
import random

#---------------- COLOUR ----------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'

#---------------- LOGO ----------------#
def logo():
    c('clear')
    print(f"""{C}
  ▄▄▄▄▄  ▄▄▄▄▄  ▄▄▄▄▄ 
 ▐█   █▌▐█   █▌▐█    
 ▐█▀▀▀  ▐█▀▀▀  ▐█▀▀▀ 
 ▐█     ▐█     ▐█▄▄▄ 
                    
{Y}     HACKING WORLD  NUMBER TRACKER TOOL
""")

#---------------- MAIN MENU ----------------#
def menu():
    logo()
    print(f"{A}[1] NUMBER DETAILS FIND")
    print(f"{A}[2] EXIT")
    print(f"{A}---------------------------------")
    choice = input(f"{Y}[?] SELECT OPTION: ")
    if choice == '1':
        number_track()
    elif choice == '2':
        exit()
    else:
        print(f"{R}[!] INVALID OPTION")
        time.sleep(1)
        menu()

#---------------- NUMBER TRACK ----------------#
def number_track():
    logo()
    c('espeak "Starting Number Details Finder"')
    number = input(f"{C}ENTER PHONE NUMBER: ")
    print(f"{Y}[+] Searching Database for {number} ...")
    time.sleep(2)
    print(f"{G}[✓] Number Found!")
    time.sleep(1)

    # Fake Data
    names = ["Rahim Khan","Tamanna Akter","Sakib Hasan","Mahiya Rahman","Arman Ali"]
    locations = ["Dhaka","Chittagong","Sylhet","Barishal","Kolkata","Delhi"]
    operators = ["GP","Robi","Airtel","Banglalink","Jio"]
    
    print(f"{C}Number        : {number}")
    print(f"Name          : {random.choice(names)}")
    print(f"Location      : {random.choice(locations)}")
    print(f"SIM Operator  : {random.choice(operators)}")
    print(f"Last Active   : {random.randint(1,30)}/0{random.randint(1,9)}/2025")
    print(f"Balance       : {random.randint(0,1000)} Taka")

    input(f"\n{Y}Press Enter To Go Back...")
    menu()

#---------------- START ----------------#
menu()