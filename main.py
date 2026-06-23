# main.py - Punctul de lansare XuX Network
import time
from colorama import Fore, Style, init
import core_config

# Initializare culori in terminal
init(autoreset=True)

def pornire_nucleu():
    print(Fore.CYAN + "=============================================")
    print(Fore.GREEN + "   PROIECTUL XuX: RETEA MULTIVALUTARA        ")
    print(Fore.GREEN + "         POLIMORFICA SUVERANA                ")
    print(Fore.CYAN + "=============================================")
    time.sleep(1)
    
    # Rulam verificarea din core_config
    if core_config.ruleaza_verificare_sistem():
        print(Fore.YELLOW + "\n[STARE] Status sistem: ONLINE (Mod Protejat)")
        print(f"[INFO] Algoritm: {core_config.NETWORK_SETTINGS['protocol']}")
        print(f"[INFO] Protectie: {core_config.NETWORK_SETTINGS['security_level']}")
        
        print("\n[MOCK] Monitorizare Sectoare Active:")
        for id_sector, nume in core_config.SECTOARE_INTEGRATE.items():
            print(f" -> Sector {id_sector:02d}: {nume} [" + Fore.GREEN + "SECURE" + Fore.RESET + "]")
    else:
        print(Fore.RED + "[CRITICAL] Eroare de structura. Autodistrugere core_config.py!")

if __name__ == "__main__":
    pornire_nucleu()
