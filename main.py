from colorama import Fore, Style
import random
import time
def redeem():
    while True:
        sleep = round(random.uniform(5, 10), 2)
        time.sleep(sleep)
        print(f"{Fore.GREEN}{Fore.BLUE}Successfully Redeemed Nitro in {sleep} seconds{Style.RESET_ALL}")
print(f'''{Fore.CYAN}
██████╗░██╗██████╗░░█████╗░  ██████╗░███████╗██████╗░███████╗███████╗███╗░░░███╗███████╗██████╗░
██╔══██╗██║██╔══██╗██╔══██╗  ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝████╗░████║██╔════╝██╔══██╗
██████╔╝██║██████╔╝██║░░██║  ██████╔╝█████╗░░██║░░██║█████╗░░█████╗░░██╔████╔██║█████╗░░██████╔╝
██╔═══╝░██║██╔══██╗██║░░██║  ██╔══██╗██╔══╝░░██║░░██║██╔══╝░░██╔══╝░░██║╚██╔╝██║██╔══╝░░██╔══██╗
██║░░░░░██║██║░░██║╚█████╔╝  ██║░░██║███████╗██████╔╝███████╗███████╗██║░╚═╝░██║███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░  ╚═╝░░╚═╝╚══════╝╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
      
      ''')
print(f"{Fore.CYAN}Starting Redeeming...")
redeem()
