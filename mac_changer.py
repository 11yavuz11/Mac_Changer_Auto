
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import time

os.system("sudo apt-get install figlet")
os.system("clear")
os.system("figlet Mac Changer Auto")

def Mac_Changer():
    second = int(input("Please enter mac replacement time: "))
    interface=input("Interface to change: ")
    while True:
        os.system("sudo macchanger -r "+interface)
        time.sleep(second)



Mac_Changer()



