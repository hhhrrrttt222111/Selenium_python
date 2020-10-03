import sys
import argparse
import _mods.menu as menu

driver = '../drivers/chromedriver.exe'

menu.main_menu()
ch = int(input("    --> "))

if ch == 1:
    menu.login()

elif ch == 2:
    menu.scraping()

elif ch == 3:
    menu.search()

elif ch == 4:
    menu.signup()

else:
    print('INVALID OPTION  \n TRY AGAIN')
    sys.exit()

