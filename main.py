#!/bin/env python3

import os


if os.geteuid() == 0:
    print("Root Mode", os.geteuid(), "is active")
else:
    print("You are running as user mode")
    print("Sorry but the script requires root to work...")
    quit(1)


from simple_term_menu import TerminalMenu
import sys
from time import *


def mainpage_sym():
    os.system('clear')
    mainpg = """
    APT Manager in Python
    Powered using simple_term_menu and others
    2023 SUFandom
"""
    print(mainpg)
    options = (["Install Package", "Uninstall Package", "Check Updates", "Configure Cached Variables", "Quit", ])
    function = [iPackage, iRemove, iUpdate, conf_Cache, quit]
    mainmenu = TerminalMenu( options, menu_cursor=("-->"))
    men_dex = mainmenu.show()
    function[men_dex]()
    mainmenu.show()



def iPackage():
    os.system("clear")
    iput = input("Enter Packages that you want to install\nType --back to go back\n-->> ")
    
    if iput == "--back":
        mainpage_sym()
    elif '--back' in iput:
        mainpage_sym()
    
    pro = os.system('sudo apt install -y {}'.format(iput))
    if pro == 0:
        print("\nProcess Ended Successfully")
        sleep(3)
        mainpage_sym()
    else:
        print("\nProcess did not end well... going back to the prompt")
        sleep(2)
        iPackage()

def iRemove():
    import re
    os.system("clear")
    iput = input("Enter Packages that you want to remove\nType --back to go back\n--force-wipe to purge\n--> ")
    
    if iput == "--back":
        mainpage_sym()
    elif '--back' in iput:
        mainpage_sym()
    
    if '--force-wipe' in iput:
        istr = re.sub('--force-wipe', '', iput)
        pro = os.system('sudo apt purge -y {}'.format(istr))
        if pro == 0:
            print("\nProcess Ended Successfully")
            sleep(3)
            mainpage_sym()
        else:
            print("\nProcess did not end well... going back to the prompt")
            sleep(2)
            iRemove()
    
    if not iput == '--force-wipe':
        pro = os.system('sudo apt remove -y {}'.format(iput))
        if pro == 0:
            print("\nPackages removed successfully")
            sleep(2)
            mainpage_sym()
        else:
            print("\nPackage was not able to be removed by APT, Probably a nonexistent package(s) in your system...")
            sleep(2)
            iRemove()

def iUpdate():
    print("Updating APT...")
    pro = os.system('sudo apt update')
    if pro == 0:
        print("Updating Database: OK")
        print("Installing Updates [If there's Any]")
        sleep(2)
    else:
        print("ERROR\nProbably a network error or just sources in /etc/apt/sources.list has an issue...\nPlease Try to Execute: sudo apt update Manually Instead to check again...")
        sleep(5)
        mainpage_sym()
    pro = os.system('sudo apt upgrade -y')
    if pro == 0:
        print("Updating Packages: OK")
        print("Going Back...")
        sleep(2)
        mainpage_sym()
    else:
        print("Could not install Packages, Probably a network error")
        sleep(2)
        mainpage_sym()

def conf_Cache():
    options = ["Clear Cached Binaries", "Back"]
    function = [clear_cache, mainpage_sym]
    conf_Menu = TerminalMenu(options, menu_cursor=("--->"))
    men_dex = conf_Menu.show()
    function[men_dex]()
    conf_Menu.show()

def clear_cache():
    print("Clearing Cache...")
    sleep(5)
    os.system("sudo apt clean -y")
    print("Done...")
    mainpage_sym()

       

mainpage_sym()