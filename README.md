

```bash
                 ,---.   .--..-./`)     ,-----.      ___    _     .-''-. ,---------.    ____       .-'''-.     ,-----.        .-''-.    ___    _ .-------.       .`````-.          .-```````-.
                |    \  |  |\ .-.')  .'  .-,  '.  .'   |  | |  .'_ _   \\          \ .'  __ `.   / _     \  .'  .-,  '.    .'_ _   \ .'   |  | ||  _ _   \     /   ,-.  \        / ,```````. \
                |  ,  \ |  |/ `-' \ / ,-.|  \ _ \ |   .'  | | / ( ` )   '`--.  ,---'/   '  \  \ (`' )/`--' / ,-.|  \ _ \  / ( ` )   '|   .'  | || ( ' )  |    (___/  |   |       |/ .-./ )  \|
                |  |\_ \|  | `-'`"`;  \  '_ /  | :.'  '_  | |. (_ o _)  |   |   \   |___|  /  |(_ o _).   ;  \  '_ /  | :. (_ o _)  |.'  '_  | ||(_ o _) /          .'  /        || \ '_ .')||
                |  _( )_\  | .---. |  _`,/ \ _/  |'   ( \.-.||  (_,_)___|   :_ _:      _.-`   | (_,_). '. |  _`,/ \ _/  ||  (_,_)___|'   ( \.-.|| (_,_).' __    _.-'_.-'         ||(_ (_) _)||
                | (_ o _)  | |   | : (  '\_/ \   ;' (`. _` /|'  \   .---.   (_I_)   .'   _    |.---.  \  :: (  '\_/ \   ;'  \   .---.' (`. _` /||  |\ \  |  | _/_  .'       _ _  ||  / .  \ 
                |  (_,_)\  | |   |  \ `"/  \  )  \| (_ (_) _) \  `-'    /  (_(=)_)  |  _( )_  |\    `-'  | \ `"/  \  ) /  \  `-'    /| (_ (_) _)|  | \ `'   /( ' )(__..--. ( ` ) ||  `-'`"` 
                |  |    |  | |   |   '. \_/``"/)  )\ /  . \ /  \       /    (_I_)   \ (_ o _) / \       /   '. \_/``".'    \       /  \ /  . \ /|  |  \    /(_{;}_)      |(_{;}_)\'._______.'/      
                '--'    '--' '---'     '-----' `-'  ``-'`-''    `'-..-'     '---'    '.(_,_).'   `-...-'      '-----'       `'-..-'    ``-'`-'' ''-'   `'-'  (_,_)-------' (_,_)  '._______.'
  ```


# NTS Cyber Bot Account Creator

A quick and fun tool developed for the "NTS Cyber Security Course" at EPITA. This script automates the creation of "bot" accounts and validates the Level 1 challenge.

## Features

- **Automated Account Creation**: Quickly create multiple accounts using a pool of funny and EPITA-related names.
- **Challenge Solver**: Automatically validates the Level 11 (Login) challenge for each created account.
- **Colorful CLI**: Features a multi-color ASCII art header and status messages.
- **Configurable**: Easily change the target URL and token via a `.env` file.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd nts_cyber
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory (or edit the existing one):
   ```env
   BASE_URL=https://.exemple.com
   TOKEN=token
   ```

## Usage

Run the script using Python 3:

```bash
python3 create_accounts.py [number_of_bots]
```

If you don't provide the number of bots as an argument, the script will prompt you for it.

## Disclaimer

This tool was created as a "little joke" for educational purposes during a cybersecurity course. It demonstrates basic automation and does not exploit any vulnerabilities other than intended course exercises.

---
*Developed in 10 minutes with the help of Gemini.*
