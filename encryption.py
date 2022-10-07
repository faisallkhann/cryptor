from cryptography.fernet import Fernet
import os
from pathlib import Path
from colorama import Fore, Back, Style

def dec(a):
    with open('fernet.key', 'rb') as fk:
        key = fk.read()
    fernet = Fernet(key)
    with open(a, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(a, 'wb') as dec_file:
        dec_file.write(decrypted)

def enc(a):
    if os.path.exists('fernet.key')==False: 
        fernetkey = Fernet.generate_key()
        with open('fernet.key', 'wb') as fk:
            fk.write(fernetkey)
    
    with open('fernet.key', 'rb') as fkk:
        fkk = fkk.read()
    fernetkey = Fernet(fkk)
    with open(a, 'rb') as file:
        original = file.read()
    encrypted = fernetkey.encrypt(original)
    with open(a, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def enc_all(a):
    for filename in os.listdir(a):
        enc(f"{a}\\{filename}")

def dec_all(a):
    for filename in os.listdir(a):
        dec(f"{a}\\{filename}")


banner0= print(Fore.RED + ''' 

 ▄████████    ▄████████ ▄██   ▄      ▄███████▄     ███      ▄██████▄     ▄████████ 
███    ███   ███    ███ ███   ██▄   ███    ███ ▀█████████▄ ███    ███   ███    ███ 
███    █▀    ███    ███ ███▄▄▄███   ███    ███    ▀███▀▀██ ███    ███   ███    ███ 
███         ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███   ███    ███     ███   ▀ ███    ███  ▄███▄▄▄▄██▀ 
███        ▀▀███▀▀▀▀▀   ▄██   ███ ▀█████████▀      ███     ███    ███ ▀▀███▀▀▀▀▀   
███    █▄  ▀███████████ ███   ███   ███            ███     ███    ███ ▀███████████ 
███    ███   ███    ███ ███   ███   ███            ███     ███    ███   ███    ███ 
████████▀    ███    ███  ▀█████▀   ▄████▀         ▄████▀    ▀██████▀    ███    ███ 
             ███    ███                                                 ███    ███ 
v1.5                                                      Developed by Faisal Khan
''')

banner = print(''' 
Please Enter Your Choice.
1. Encrypt any file.
2. Decrypt any file.
3. Encrypt all Files inside a directory.
4. Decrypt all Files inside a directory.

Note- Input Integers Only.
''')

choice=int(input("Please Enter Your Choice: "))

if(choice==1):
    file=input("Enter the file Name/Path: ")
    enc(file)
    print("Encryption Completed.")
elif(choice==2):
    file=input("Enter the file Name/Path: ")
    dec(file)
    print("Decryption Completed.")
elif(choice==3):
    Directory=input("Enter the Directory Name: ")
    enc_all(Directory)
    print("Encryption Completed.")
elif(choice==4):
    Directory=input("Enter the Directory Name: ")
    dec_all(Directory)
    print("Decryption Completed.")
else:
    print("Invalid Input!!!")
