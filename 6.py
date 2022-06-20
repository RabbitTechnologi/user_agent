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
    
x = UserAgent(family='opera')
b1 =x.random()
b2 = x.random()
b3 = x.random()
b4 = x.random()
b5 = x.random()

#randomly printing any 5 useragent
os.system("clear")
print(logo)
print("\x1b[1;92m ●\033[1;90m USER AGENT SAVE IN >> opera-ua.txt")
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

open("opera-ua.txt","a").write(b1+'\n')
open("opera-ua.txt","a").write(b2+'\n')
open("opera-ua.txt","a").write(b3+'\n')
open("opera-ua.txt","a").write(b4+'\n')
open("opera-ua.txt","a").write(b5+'\n')




