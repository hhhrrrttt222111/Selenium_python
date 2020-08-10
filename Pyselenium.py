import sys
import argparse
from os import system, name


def main_menu():
    clear_screen()
    print(f'''
CHOOSE OPTION :

    Login Automation          [1]  
    Scarping with Selenium    [2]    
    Search                    [3]    
    Sign Up Automation        [4]   

    ''')


ch = int(input("    --> "))



def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')