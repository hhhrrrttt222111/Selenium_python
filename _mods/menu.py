from os import system, name
import sys
import LOGINS.facebook_login as fb
import LOGINS.google_login as gl
import LOGINS.pinterest_login as pint
import LOGINS.twitter_login as twt
import LOGINS.spotify_login as sp

import SCRAPING.Billboard_100 as billboard
import SCRAPING.CodeChef as codechef
import SCRAPING.Covid_deaths as covid
import SCRAPING.DJ_Mag_100 as djmag
import SCRAPING.IMDB_top_250 as imdb
import SCRAPING.Wikipedia_search as wiki

import SEARCHES.Amazon_search as amazon
import SEARCHES.Flipkart_search as flipkart
import SEARCHES.Youtube_video_names as yt

import SIGNUP.facebook_signup as fbsign
import SIGNUP.swiggy_signup as swiggy

def main_menu():
    clear_screen()
    print(f'''
CHOOSE OPTION :

    Login Automation          [1]  
    Scarping with Selenium    [2]    
    Search                    [3]    
    Sign Up Automation        [4]   

    ''')


def login():
    def logins_menu():
        clear_screen()
        global ch
        print(f'''
    CHOOSE OPTION :
    
        Facebook      [1]  
        Google        [2]    
        Pinterest     [3]    
        Spotify       [4]   
        Twitter       [5]   
    
        ''')

        ch = int(input("    --> "))
        print('\n')

    logins_menu()

    if ch == 1:
        fb.fb_login()

    elif ch == 2:
        gl.google_login()

    elif ch == 3:
        pint.pinterest_login()

    elif ch == 4:
        sp.spotify_login()

    elif ch == 5:
        twt.twitter_login()

    else:
        print('INVALID OPTION  \n TRY AGAIN')
        sys.exit()


def scraping():
    def scraping_menu():
        clear_screen()
        global ch
        print(f'''
    CHOOSE OPTION :

        Billboard Top Songs     [1]  
        CodeChef Questions      [2]    
        Covid Deaths            [3]    
        DJ Mag Top 100          [4]   
        IMDB Top movies         [5]  
I       Wikipedia               [6]  

        ''')

        ch = int(input("    --> "))
        print('\n')

    scraping_menu()

    if ch == 1:
        billboard.billboard()

    elif ch == 2:
        codechef.codechef()

    elif ch == 3:
        covid.covid()

    elif ch == 4:
        djmag.djmag()

    elif ch == 5:
        imdb.imdb()

    elif ch == 6:
        wiki.wikipedia()

    else:
        print('INVALID OPTION  \n TRY AGAIN')
        sys.exit()


def search():
    def search_menu():
        clear_screen()
        global ch
        print(f'''
    CHOOSE OPTION :

        Amazon Search         [1]  
        Flipkart              [2]    
        Youtube Search        [3]    

        ''')

        ch = int(input("    --> "))
        print('\n')

    search_menu()

    if ch == 1:
        amazon.amazon()

    elif ch == 2:
        flipkart.flipkart()

    elif ch == 3:
        yt.youtube()

    else:
        print('INVALID OPTION  \n TRY AGAIN')
        sys.exit()


def signup():
    def signup_menu():
        clear_screen()
        global ch
        print(f'''
    CHOOSE OPTION :

        Facebook Signup      [1]  
        Swiggy Signup        [2]    

        ''')

        ch = int(input("    --> "))
        print('\n')

    signup_menu()

    if ch == 1:
        fbsign.fb_signup()

    elif ch == 2:
        swiggy.swiggy()

    else:
        print('INVALID OPTION  \n TRY AGAIN')
        sys.exit()


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')