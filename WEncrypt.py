import os
import sys
import time
import argparse
from tkinter import filedialog
from cryptography.fernet import Fernet

w = '\033[37m' #white
R = '\033[31m' #red
C = '\033[36m' #cyan
lr = '\033[91m' #lightred

def encrypt_file(file_path, key, make_copy):
    with open(file_path, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    if make_copy:
        with open(file_path + ".encrypted", 'wb') as f:
            f.write(encrypted)
    else:
        with open(file_path + ".encrypted", 'wb') as f:
            f.write(encrypted)
        os.remove(file_path)

def encrypt_folder(folder_path, make_copy):
    key = Fernet.generate_key()
    file_path = os.path.abspath(os.path.dirname(__file__))
    output_path = os.path.join(file_path, 'key.txt')
    with open(output_path, 'wb') as key_file:
        key_file.write(key)
        print(f"{C}> {w}Encryption key: {key}")
        print(f"{C}> {w}Encryption key location: {output_path}")
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key, make_copy)

def start(folder_path, make_copy):
    confirm = input(f"{C}> {w}Do you really want to {lr}ENCRYPT{w} all files in the folder? (Y/N): ")
    if confirm.capitalize() == "Y":
        encrypt_folder(folder_path, make_copy)
        print(f"{R}Files Encrypted.")
        print(f"{w}Press '{R}Enter{w}' to exit.")
        input()
    else:
        print(f"{R}Cancelled{w}")
        time.sleep(2)
        exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt files in a folder')
    parser.add_argument('-f', '--folder_path', help='Path to folder to encrypt')
    parser.add_argument('-c', '--copy', help='Whether to make copies of the files or encrypt them', choices=['y', 'n'])
    args = parser.parse_args()

    if not args.folder_path:
        folder_path = filedialog.askdirectory()
    else:
        folder_path = args.folder_path

    if not args.copy:
        copy_or_encrypt = input(f"{C}> {w}Do you want to make copies or encrypt original files? (Y/N): ")
        if copy_or_encrypt.capitalize() == "Y":
            make_copy = True
        elif copy_or_encrypt.capitalize() == "N":
            make_copy = False
        else:
            print(f"{R}Invalid input.")
            time.sleep(2)
            exit()
    else:
        make_copy = args.copy == 'y'

    start(folder_path, make_copy)