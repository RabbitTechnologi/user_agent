W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
import os
try:
    import my_fake_useragent
except ImportError:
    print('\n [✓] installing pip wait !...\n')
    os.system('pip install my_fake_useragent')
from my_fake_useragent import UserAgent
import random
logo = """
       \x1b[1;91m▒█▒█▒▄█▀▀█░▐█▀▀▒▐█▀▀▄   ▒█▒█░▐█▀▀▀─░▐█▀▀▒██▄░▒█▌▒█▀█▀█       
       \x1b[1;97m▒█▒█▒▀▀█▄▄░▐█▀▀▒▐█▒▐█   ▒█▒█░▐█░▀█▌░▐█▀▀▒▐█▒█▒█░░░▒█░░       
       \x1b[1;94m▒▀▄▀▒█▄▄█▀░▐█▄▄▒▐█▀▄▄   ▒▀▄▀░▐██▄█▌░▐█▄▄▒██░▒██▌░▒▄█▄░ 
    \033[93;1m    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬     
   \x1b[1;91m    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{ \033[1;90mAUTHOR \x1b[1;92m ● \033[1;90mK4LONG666\x1b[1;91m }▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬     
   \x1b[1;97m    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{ \033[1;90mFACEBOOK \x1b[1;92m ● \033[1;90mA-KENZI\x1b[1;97m }▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬     
   \x1b[1;94m    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{ \033[1;90mGITHUB \x1b[1;92m ● \033[1;90mK4LONG666\x1b[1;94m }▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    """
    
x = UserAgent(family='chrome')
b1 =x.random()
b2 = x.random()
b3 = x.random()
b4 = x.random()
b5 = x.random()
b6 = x.random()
b7 = x.random()
b8 = x.random()
b9 = x.random()
b10 = x.random()

#randomly printing any 5 useragent
os.system("clear")
print(logo)
print("\x1b[1;92m ●\033[1;90m USER AGENT SAVE IN >> safari-ua.txt")
print("\033[1;90m")
print(b1)
print("")
print(b2)
print("")
print(b3)
print("")
print(b4)
print("")
print(b5)
print("")
print(b6)
print("")
print(b7)
print("")
print(b8)
print("")
print(b9)
print("")
print(b10)
print("")


open("chrome-ua.txt","a").write(b6+'\n')
open("chrome-ua.txt","a").write(b7+'\n')
open("chrome-ua.txt","a").write(b8+'\n')
open("chrome-ua.txt","a").write(b9+'\n')
open("chrome-ua.txt","a").write(b10+'\n')




