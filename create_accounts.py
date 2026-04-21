import requests
import time
import sys
import random
import os
from datetime import datetime
from colorama import init, Fore, Style
from dotenv import load_dotenv

# Initialize colorama
init(autoreset=True)

# Load environment variables
load_dotenv()

# Configuration
BASE_URL = os.getenv("BASE_URL", "https://ranku1.exegide.com")
TOKEN = os.getenv("TOKEN", "EXE30")

# Multicolor ASCII ART
RAW_ASCII = r"""
                 ,---.   .--..-./`)     ,-----.      ___    _     .-''-. ,---------.    ____       .-'''-.     ,-----.        .-''-.    ___    _ .-------.       .`````-.          .-```````-.                         
                |    \  |  |\ .-.')  .'  .-,  '.  .'   |  | |  .'_ _   \\          \ .'  __ `.   / _     \  .'  .-,  '.    .'_ _   \ .'   |  | ||  _ _   \     /   ,-.  \        / ,```````. \                        
                |  ,  \ |  |/ `-' \ / ,-.|  \ _ \ |   .'  | | / ( ` )   '`--.  ,---'/   '  \  \ (`' )/`--' / ,-.|  \ _ \  / ( ` )   '|   .'  | || ( ' )  |    (___/  |   |       |/ .-./ )  \|                        
                |  |\_ \|  | `-'`"`;  \  '_ /  | :.'  '_  | |. (_ o _)  |   |   \   |___|  /  |(_ o _).   ;  \  '_ /  | :. (_ o _)  |.'  '_  | ||(_ o _) /          .'  /        || \ '_ .')||                        
                |  _( )_\  | .---. |  _`,/ \ _/  |'   ( \.-.||  (_,_)___|   :_ _:      _.-`   | (_,_). '. |  _`,/ \ _/  ||  (_,_)___|'   ( \.-.|| (_,_).' __    _.-'_.-'         ||(_ (_) _)||                        
                | (_ o _)  | |   | : (  '\_/ \   ;' (`. _` /|'  \   .---.   (_I_)   .'   _    |.---.  \  :: (  '\_/ \   ;'  \   .---.' (`. _` /||  |\ \  |  | _/_  .'       _ _  ||  / .  \ ||                        
                |  (_,_)\  | |   |  \ `"/  \  )  \| (_ (_) _) \  `-'    /  (_(=)_)  |  _( )_  |\    `-'  | \ `"/  \  ) /  \  `-'    /| (_ (_) _)|  | \ `'   /( ' )(__..--. ( ` ) ||  `-'`"` ||                        
                |  |    |  | |   |   '. \_/``"/)  )\ /  . \ /  \       /    (_I_)   \ (_ o _) / \       /   '. \_/``".'    \       /  \ /  . \ /|  |  \    /(_{;}_)      |(_{;}_)\'._______.'/                        
                '--'    '--' '---'     '-----' `-'  ``-'`-''    `'-..-'     '---'    '.(_,_).'   `-...-'      '-----'       `'-..-'    ``-'`-'' ''-'   `'-'  (_,_)-------' (_,_)  '._______.'                         
"""

COLORS = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def print_multicolor_ascii():
    lines = RAW_ASCII.strip("\n").split("\n")
    for i, line in enumerate(lines):
        color = COLORS[i % len(COLORS)]
        print(f"{color}{line}")
    print(f"\n{Fore.WHITE}{Style.BRIGHT}                            NiqueTaSoeur 2.0 - EPITA Edition\n")

# Dictionary of EPITA / Funny names
EPITA_REFS = [
    "pfa=paf", "TomNookleRat", "one_crepe_please", "Sweating_Koala", 
    "Acu_killed_me", "Determined_Moulinette", "Norminette_Hater", "Pass_the_Bocal", 
    "Log_Error_42", "VBA_is_Life", "The_G_Stack", "Imaginary_Valedictorian",
    "Sleeping_in_Lecture", "Coffee_Machine_Broken", "Forge_Ticket_Ignored",
    "Bobby_Tables", "Sudo_Make_Me_A_Coffee", "Budget_Mr_Robot", 
    "Git_Push_Force_And_Pray", "StackOverFlow_CopyPaste", "SyntaxError_Enjoyer",
    "NullPointerException", "Little_Kernel", "Public_Wifi_Hacker",
    "Rubber_Duck", "Numpad_Warrior", "Infinite_Ping", "Hell_Lag",
    "Azerty_Keyboard_In_Hell", "Right_Double_Click", "Alt_F4_Warrior",
    "Segfault_Master", "Docker_Is_Heavy", "Python_Lover_69", "Assembly_God"
]

ADMIN_VARIANTS = [
    "admin", "adm1n", "administrator", "root", "toor", "superuser", 
    "master", "system", "admin_local", "bocal_admin", "acu_admin",
    "admin123", "ADMIN", "Admin", "root_epita", "sys_admin", "staff_admin",
    "it_support", "webmaster", "operator", "daemon"
]

NAMES_POOL = EPITA_REFS + ADMIN_VARIANTS

def solve_challenge_11(session, bot_username):
    """Automates the Level 11 challenge validation."""
    verify_url = f"{BASE_URL}/challenge_verification"
    jwt_token = session.cookies.get('token')
    if not jwt_token: return False

    now = datetime.now()
    payload = {
        "challenge_name": "ch - 11: Login",
        "username": "admin",
        "password": "admin",
        "word": None,
        "time": now.strftime("%H:%M:%S"),
        "date": now.strftime("%d/%m/%Y")
    }
    
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"
    }
    
    try:
        response = session.post(verify_url, json=payload, headers=headers, timeout=10)
        return response.status_code == 200 and response.json().get("status") == "success"
    except Exception:
        return False

def create_and_run_bot(username):
    """Creates a new account and attempts to solve the initial challenge."""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Origin": BASE_URL,
        "Referer": f"{BASE_URL}/"
    }
    
    session = requests.Session()
    session.headers.update(headers)

    try:
        resp = session.post(f"{BASE_URL}/create_account", json={"username": username, "token": TOKEN}, timeout=10)
        if resp.status_code == 200 and resp.json().get("status") == "success":
            print(f"{Fore.CYAN}[*] {username} : Account created.")
            if solve_challenge_11(session, username):
                print(f"{Fore.GREEN}[+] {username} : Challenge succeeded.")
                logout_resp = session.post(f"{BASE_URL}/logout", json={}, timeout=10)
                if logout_resp.status_code == 200:
                    print(f"{Fore.MAGENTA}[OK] {username} : Session validated and closed.")
                    return True
        elif resp.status_code == 409:
            print(f"{Fore.YELLOW}[-] {username} : Already exists.")
    except Exception as e:
        print(f"{Fore.RED}[!] Bot error {username} : {e}")
    
    return False

def main():
    print_multicolor_ascii()
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            count = 1
    else:
        try:
            val = input(f"{Fore.WHITE}How many bots do you want to send? : ")
            count = int(val)
        except ValueError:
            print(f"{Fore.RED}[!] Invalid number.")
            return

    random.shuffle(NAMES_POOL)
    final_names = []
    for i in range(count):
        base_name = NAMES_POOL[i % len(NAMES_POOL)]
        suffix = f"_{i // len(NAMES_POOL) + 1}" if i >= len(NAMES_POOL) else ""
        final_names.append(f"{base_name}{suffix}")

    print(f"{Fore.YELLOW}[*] Selected bots: {Fore.WHITE}{', '.join(final_names)}")
    print(f"\n{Fore.BLUE}[*] Launching operation 'Total Admin Invasion' ({count} bots)...\n")

    success_count = 0
    for name in final_names:
        if create_and_run_bot(name):
            success_count += 1
        time.sleep(0.7)

    print(f"\n{Fore.GREEN}[FINISH] {success_count}/{count} bots have joined the ranking!")

if __name__ == "__main__":
    main()
