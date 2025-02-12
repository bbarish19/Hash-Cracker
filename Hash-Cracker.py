import hashlib
import tkinter as tk
from tkinter import filedialog

ASCII_ART = """
8888888888888888888888888888888888888888888888888888888888888888888888
8888888888888888888888888888888888888888888888888888888888888888888888
888888888888888888888888888888P""  ""988888888888888888888888888888888
888888888888888888888P"88888P          988888"988888888888888888888888
888888888888888888888  "9888            888P"  88888888888888888888888
88888888888888888888888bo "9  d8o  o8b  P" od8888888888888888888888888
88888888888888888888888888bob 98"  "8P dod8888888888888888888888888888
88888888888888888888888888888    db    8888888888888888888888888888888
8888888888888888888888888888888      888888888888888888888888888888888
8888888888888888888888888888P"9bo  odP"9888888888888888888888888888888
8888888888888888888888888P" od88888888bo "9888888888888888888888888888
88888888888888888888888   d88888888888888b   8888888888888888888888888
888888888888888888888888oo8888888888888888oo88888888888888888888888888
8888888888888888888888888888888888888888888888888888888888888888888888
"""

def welcome_screen():
    """Displays a welcome screen with ASCII art and some nice formatting."""
    print("\n" + "="*70)
    print(" "*21 + "WELCOME TO THE HASH CRACKER")
    print("-"*70)
    print(ASCII_ART)
    print("-"*70)
    print(" "*19 +"This tool lets you crack hashes!")
    print(" "*17 + "Program created by: Benjamin Barish")
    print("="*70)

import hashlib
import tkinter as tk
from tkinter import filedialog
import os

def validate_choice(prompt, choices):
    while True:
        choice = input(prompt).strip().lower()
        if choice in choices:
            return choice
        print("[!] Invalid choice. Please try again.")

def validate_file_path(prompt):
    while True:
        file_path = input(prompt).strip()
        if os.path.isfile(file_path):
            return file_path
        print("[!] Invalid file path. Please enter a valid file path.")

def crack_hash(hash_to_crack, hash_type, wordlist_file):
    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
            for word in file:
                word = word.strip()
                hashed_word = hashlib.new(hash_type, word.encode()).hexdigest()
                
                if hashed_word == hash_to_crack:
                    print(f"[+] Password found: {word}")
                    return word
        
        print("[-] Password not found in wordlist.")
        return None
    except FileNotFoundError:
        print("[!] Wordlist file not found.")
    except ValueError:
        print("[!] Invalid hash type provided.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

def try_all_hashes(hash_to_crack, wordlist_file):
    hash_types = ['md5', 'sha1', 'sha256', 'sha512']
    for hash_type in hash_types:
        print(f"[*] Trying hash type: {hash_type}")
        result = crack_hash(hash_to_crack, hash_type, wordlist_file)
        if result:
            print(f"[+] Successfully cracked using {hash_type}!")
            return result
    print("[-] No matching hash found with common algorithms.")
    return None

def get_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path if file_path else None

if __name__ == "__main__":
    while True:
        welcome_screen()  # Display the welcome screen with ASCII art and description

        hash_source = validate_choice("Do you want to enter the hash (M)anually or select a (F)ile? (M/F): ", ["m", "f"])
        
        if hash_source == "f":
            while True:
                hash_file = get_file_path()
                if hash_file and os.path.isfile(hash_file):
                    try:
                        with open(hash_file, 'r', encoding='utf-8') as f:
                            hash_to_crack = f.read().strip()
                        break
                    except FileNotFoundError:
                        print("[!] Hash file not found.")
                else:
                    print("[!] Invalid file selection. Please try again.")
        else:
            hash_to_crack = input("Enter the hash to crack: ").strip()
        
        hash_type = validate_choice("Enter hash type (md5, sha1, sha256, sha512, or 'auto' to try all): ", ["md5", "sha1", "sha256", "sha512", "auto"])
        
        file_choice = validate_choice("Do you want to enter the wordlist path (M)anually or select a (F)ile? (M/F): ", ["m", "f"])
        
        if file_choice == "f":
            while True:
                wordlist_file = get_file_path()
                if wordlist_file and os.path.isfile(wordlist_file):
                    break
                print("[!] Invalid file selection. Please try again.")
        else:
            wordlist_file = validate_file_path("Enter wordlist file path: ")
        
        if hash_type == "auto":
            try_all_hashes(hash_to_crack, wordlist_file)
        else:
            crack_hash(hash_to_crack, hash_type, wordlist_file)
        
        choice = validate_choice("Do you want to crack another hash? (Y/N): ", ["y", "n"])  # Compare with lowercase 'y' and 'n'
        if choice != 'y':
            print("Goodbye!")
            break



