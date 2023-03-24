import os
import tkinter as tk
import time
from tkinter import filedialog
from cryptography.fernet import Fernet

w = '\033[37m' #white
R = '\033[31m' #red
C = '\033[36m' #cyan
lr = '\033[91m' #lightred

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    with open(os.path.splitext(file_path)[0], 'wb') as f:
        f.write(decrypted)
    os.remove(file_path)

def decrypt_folder(folder_path):
    file_path = os.path.abspath(os.path.dirname(__file__))
    output_path = os.path.join(file_path, 'key.txt')
    try:
        with open(output_path, 'rb') as key_file:
            key = key_file.read()
            print(f"{C}> {w}Deryption key: {key}")
            print(f"{C}> {w}Decryption key location: {file_path}")
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.endswith(".encrypted"):
                    decrypt_file(file_path, key)
    except:
        print(f"{C}> {R}Error: Decrypt key file not found!{w}")
        
def start():
    folder_path = filedialog.askdirectory()
    confirm = input(f"{C}> {w}Do you really want to {lr}DECRYPT{w} all files in the folder?{w}(Y/N): ")
    if confirm.capitalize() == "Y":
        decrypt_folder(folder_path)
        print(f"{R}Files Decrypted.")
        print(f"{w}Press '{R}Enter{w}' to exit.")
        input()
    else:
        print(f"{R}Cancelled!{w}")
        time.sleep(2)
        exit()

if __name__ == '__main__':
    start()