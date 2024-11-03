from ip.scoutip import ipinfo
from ip.ip2add import ip_to_address
from ai.scout_ai import ai_search
from ai.scout_ai import found_info
from search.gsearch import search_google 
from phone.lookup import phonenum_lookup
from user.usercheck import find_username
from cfg import title, version
from colorama import style, fore
from time import sleep

print({Fore.Blue}str(title){Style.RESET_ALL})
print(version)
while True:
    option = input("[>] ")
    if option == 1:
        m_ip = input("Enter IP:\n[>] ")
        print(ipinfo(m_ip))
    elif option == 2:
        a_ip = input("Enter IP:\n[>] ")
        print(ip_to_address(a_ip))
    elif option == 3:
        