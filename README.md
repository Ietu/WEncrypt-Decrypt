pip install -r requirements.txt

# WEncrypt-Decrypt

Encrypts/decrypts all files in a folder using Fernet encryption. Generates a key in a text file for safety reasons.

## DISCLAIMER
This encryption script is provided for securing your ***PERSONAL*** files and should not be used for anything else.

Use at your own risk! Even though this has always worked for me I can never quarantee 100% that it can't have any errors.


## Info

Python Encryptor and Decryptor, part of upcoming Wratheon RAT tool. Easy to implement into a project to encrypt or decrypt files.


If Encryptor is run with ***no arguments***, opens a file dialog to select folder to encrypt, but it can be run with arguments for reasons.

***Decryptor is only with filedialog currently.***

## Usage
With arguments: `python WEncrypt.py [-f FOLDER_PATH] [-c {Y,N}]`

Example: `python WEncrypt.py -f E:\path\to\folder\THIS -c n` would encrypt everything in the `THIS` folder without making copies of original files.




optional arguments:
  `-h`, `--help` | show this help message and exit
  
  
  `-f FOLDER_PATH`, `--folder FOLDER_PATH` | The path to the folder containing the files to encrypt.
                        
                        
  `-c {y,n}`, `--copy {y,n}` | Whether to create copies of the original files or encrypt them directly. Enter Y to make copies or N to encrypt the original files.


## Example without arguments
https://user-images.githubusercontent.com/54209182/227652805-8d9ae135-7d3d-497c-8d27-88ed52bc441b.mp4

