# Hash-Cracker
Overview:
This tool allows you to crack hashes using a wordlist. It supports common hash algorithms (MD5, SHA-1, SHA-256, SHA-512) and offers the option to try all hash types automatically. You can enter the hash to crack manually or select a file, and you can either manually provide the path to your wordlist or select a file as well.

Features:
Support for multiple hash types: MD5, SHA-1, SHA-256, SHA-512
Option to input the hash manually or select a file containing the hash
Option to input the wordlist manually or select a file
Automatic hash type detection if the "auto" option is selected
Error handling for invalid input and file paths
User-friendly prompts and clear output
Requirements:
Python 3.x
tkinter (for file dialog)
Access to a wordlist file (a plain text file with potential passwords)

Installation:
Ensure you have Python 3.x installed on your machine.
Install tkinter if not already installed (usually included by default):
pip install tk
Clone or download the Hash Cracker script to your system.

Usage:
Run the script hash_cracker.py (or the name of the script you have).
The program will display an ASCII welcome screen and prompt you to either:
Enter the hash manually
Select a file containing the hash
You will then be prompted to choose the hash type (md5, sha1, sha256, sha512) or select "auto" to let the program try all hash types.
After that, you'll be asked to select the wordlist file to use or provide its path manually.
The program will then attempt to crack the hash using the wordlist. If successful, it will print the cracked password.
Once the cracking attempt is finished, you will be asked if you want to crack another hash. Enter "Y" to continue or "N" to exit.

Troubleshooting:
If you encounter a FileNotFoundError, ensure that the file path you provide for the hash or wordlist is correct.
If the program doesn't recognize your input, make sure to enter "Y" or "N" in uppercase or lowercase.
If the hash isn't cracked, try using a larger or more comprehensive wordlist.
