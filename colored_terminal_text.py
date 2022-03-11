import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print(Fore.BLACK + Back.CYAN + " Text color ")

print(Fore.YELLOW + Back.BLUE+" One " +
      Fore.WHITE + Back.GREEN+" Two " +
      Fore.BLUE + Back.YELLOW+" THREE ")
