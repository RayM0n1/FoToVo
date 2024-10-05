import os
import sys
import platform
import time
import socket  # To get the device IP
import subprocess  # To install packages
import sys

# Function to install a package if it's not already installed
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Attempt to import colorama and install if it is not present
try:
    from colorama import Fore, Style, init  # For colored text
    init(autoreset=True)
except ImportError:
    print("colorama not found. Installing...")
    install('colorama')
    from colorama import Fore, Style, init  # Import again after installation
    init(autoreset=True)

# ASCII Art
def display_ascii_art():
    print(Fore.MAGENTA + r"""
     _,---.     _,.---._    ,--.--------.   _,.---._           ,-.-.   _,.---._     
  .-`.' ,  \  ,-.' , -  `. /==/,  -   , -\,-.' , -  `.  ,--.-./=/ ,/ ,-.' , -  `.   
 /==/_  _.-' /==/_,  ,  - \\==\.-.  - ,-./==/_,  ,  - \/==/, ||=| -|/==/_,  ,  - \  
/==/-  '..-.|==|   .=.     |`--`\==\- \ |==|   .=.     \==\,  \ / ,|==|   .=.     | 
|==|_ ,    /|==|_ : ;=:  - |     \==\_ \|==|_ : ;=:  - |\==\ - ' - /==|_ : ;=:  - | 
|==|   .--' |==| , '='     |     |==|- ||==| , '='     | \==\ ,   ||==| , '='     | 
|==|-  |     \==\ -    ,_ /      |==|, | \==\ -    ,_ /  |==| -  ,/ \==\ -    ,_ /  
/==/   \      '.='. -   .'       /==/ -/  '.='. -   .'   \==\  _ /   '.='. -   .'   
`--`---'        `--`--''         `--`--`    `--`--''      `--`--'      `--`--''     
    """)

    # Title
    print(Fore.MAGENTA + "Madye - by RayM0n98\n")

# Simulated loading animation
def loading_animation():
    print(Fore.MAGENTA + "Loading", end="")
    for _ in range(5):  # Simulate loading with dots
        print(Fore.MAGENTA + ".", end="")
        time.sleep(0.5)
    print("\n")  # Move to the next line after loading is done

# Function to list all files including hidden and system files
def check_all_files():
    # Use a root directory as an example (change if needed)
    root_dir = "C:/" if platform.system() == "Windows" else "/"
    
    print(Fore.MAGENTA + f"\nChecking all files on device ({root_dir}):")
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            print(os.path.join(root, file))
        time.sleep(0.01)  # To prevent overwhelming the user with file names at once

# Function to get the device's IP address
def check_device_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    print(Fore.MAGENTA + f"\nDevice Name: {hostname}")
    print(Fore.MAGENTA + f"IP Address: {ip_address}")

def main():
    loading_animation()  # Display loading animation before starting the multitool
    display_ascii_art()  # Display ASCII art and title at the beginning
    
    while True:
        print(Fore.MAGENTA + "\nWelcome to the FoToVo!")  # Updated name for the multitool
        print(Fore.MAGENTA + "1. Check all files on the device (including hidden and system files)")
        print(Fore.MAGENTA + "2. Check device IP")
        print(Fore.MAGENTA + "3. Exit")

        choice = input(Fore.MAGENTA + "Enter your choice (1/2/3): ")

        if choice == "1":
            check_all_files()
        elif choice == "2":
            check_device_ip()
        elif choice == "3":
            print(Fore.MAGENTA + "Exiting the FoToVo. Goodbye!")
            sys.exit()
        else:
            print(Fore.MAGENTA + "Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
