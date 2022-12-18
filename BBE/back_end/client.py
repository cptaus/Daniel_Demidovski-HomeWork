from back_end.manager import program as admin_program
from back_end.manager import show_routes, find_route
from back_end.core import console_cleaner as clean_screen
from back_end.core import wait_for_user_continue as wait_for_user
import datetime
import socket
from getpass import getpass

# for logging data
host = socket.gethostname()
ip_address = socket.gethostbyname(host)


def logo():
    logo_draw = \
    f"""     
    └▀██████████████▄                                                          
         ╙▀▀▀  ▓▀▀▀████░                                          
               ▄▄▄▄▄███                      ██▌  ██████▄                       
             ▐█████████▄    ▄████▄   ▄████▄ █████ ██▌ ▐██   ██   ▐██  ▄████▄    
            ▄████▀▀▀▀████ ███▄▄▄▄██  ██▄▄▀   ██▌  ██████▄   ██▌  ▐██  ██▄      
          ▄████▀     ████░███▀▀▀▀▀▀▌  ▀███▄  ██▌  ██▌  ▐██  ██▌  ▐██     ██▄    
      ▄▄████████████████▀ ▀██▄▄▄▄█▄  ▄█▄▄██  ██▌  ███▄███▀  ▀██▄▄██▌  ██▄▄██    
     ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀     ▀▀▀▀   ▀▀   ▀▀▀▀▀▀▀    ▀▀▀▀▀▀    ▀▀▀▀
---------------------------------------------------------------------------------
    Welcome! Please chose option from the menu below. {datetime.datetime.utcnow().strftime('%H:%M %d-%m-%Y')}"""

    return logo_draw


def main_manu():
    context = f"""
    1. Login
    2. Timetable"""
    return context


def client_manu(data):
    while True:
        clean_screen()
        context = f"""
        1. Show all routes
        2. Search route by line
        3. Report delay
        exit. Exit the program"""
        print(context)
        selected = option_selector(input("Please select number from the option list above: "), ["1", "2", "3", "exit"])
        if not selected:
            continue
        if selected == "1":
            show_routes(data)
            wait_for_user()
        if selected == "2":
            find_route(data)
            wait_for_user()
        if selected == "3":
            pass
        if selected == "exit":
            return


def option_selector(selection, options: list):
    if not selection.isdigit():
        print(f"Please chose between the numbers above... {selection} is not a number.")
        return False
    if selection not in options:
        print(f"Please chose from the list. {selection} not in the list.")
        return False
    return selection


def login(data):
    __attempts = 0
    while __attempts <= 3:
        if getpass("Please insert passkey: ") != "RideWithUs!":
            clean_screen()
            print(f"INCORRECT PASSWORD! {3 - __attempts} attempts left.")
            __attempts += 1
        else:
            clean_screen()
            print("Welcome manager!")
            admin_program(data)
            break
    if __attempts == 3+1:
        clean_screen()
        print(f"3 LOGIN ATTEMPTS, EXITING. YOUR IP {ip_address} WAS LOGGED")
        return False


def main_program(data, debug=False):
    clean_screen()
    if debug:
        print("DEBUG MODE IS ON! HOPE IT IS NOT THE PRODUCTION >:(")
    print(logo())
    while True:
        print(main_manu())
        selected = option_selector(input("Please select number from the option list above: "), ["1", "2"])
        if not selected:
            continue
        if selected == "1":
            login(data)
        if selected == "2":
            client_manu(data)
        break
