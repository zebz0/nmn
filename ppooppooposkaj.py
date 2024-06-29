import os, requests, random, threading
from user_agent import *
try:
    import pazok
except:
    os.system('pip install pazok')             
#====الوان====
Z = '\033[1;31m'  # أحمر
X = '\033[1;33m'  # أصفر
F = '\033[2;32m'  # أخضر
C = "\033[1;97m"  # أبيض
B = '\033[2;36m'  # أزرق
Y = '\033[1;34m'  # أزرق داكن
W = '\033[0;37m'  # رمادي
e = "\u001b[38;5;242m" #رمادي داكن
m = "\u001b[38;5;15m" #ابيض
E = "\u001b[38;5;8m" #رمادي فاتح
p = '\x1b[1m'#عريض
#====الوان====
logo ="""\033[2;36m⠀\x1b[1m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⠻⣿⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⡿⠉⠀⣀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠋⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡝⠛⠉⠉⠉⠉⠉⠻⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠜⢻⡿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢋⣽⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣠⡿⠋⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣰⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⢀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⠀⠀⠀⠈⠉⠛⠿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣷⣶⣤⡔⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣝⢿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⠛⣛⣛⣂⣀⣀⣀⠀⣀⣀⣀⣀⣀⣀⡀⣈⣉⣀⣀⣀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⠋⢉⡻⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⠛⢻⣿⡿⠀⠛⣿⡟⠛⢻⣿⡇⠙⣿⡟⠛⢻⣿⡄⣿⣿⠛⣻⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⡄⠈⢿⣷⡹⣿⣿⣿⣿⣿⡃⠀⢀⣴⣿⠏⠀⠀⠀⣿⣷⣶⠀⠀⠀⠀⣿⣷⣶⣾⣿⠁⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣧⠀⠘⣿⣿⣌⢻⣿⣿⡟⠁⣠⣾⣟⣁⣰⣶⠀⠀⣿⡇⠀⢰⣶⡆⠀⣿⣇⠀⣸⣿⠇⣠⣿⣟⣁⣰⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣧⠀⠘⣿⣿⣷⣍⢿⠀⠀⠛⠛⠛⠛⠛⠛⠀⠛⠛⠛⠛⠛⠛⠃⠛⠛⠛⠛⠛⠋⠀⠛⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⠀⠀⠻⣿⣿⣷⣜⡻⠿⣿⣿⣿⣿⣶⡦⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠷⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
print(logo)
#====لوكو====
#ملاحضه تم اضافت التوكن و الايدي لمعرفت من صاد في الاداه 
tokenzebz = "7042398014:AAHwjhRdiGzeOFHRc95AFO0njkPaRrhoASw"
idzebz = 6060332252
token = input(f' {E} Enter The {B}Token :{E} ')
id = input(f' {E} Enter The {B}ID :{E} ')
TOP = """
تم تشغيل الاداه
"""
po=[
"الشخص",f"tg://openmessage?user_id={id}",
            ]
pazok.tele_ms(tokenzebz,idzebz,txt=TOP,buttons=po)            
os.system('clear')
print("—"*60)
print(logo)
print("—"*60)

ses=requests.Session()
url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
try:
    prox = requests.get(url).text
    open('.Proxs.txt', 'w').write(prox) 
except Exception as e:
    print('\x1b[1;91mError: \x1b[96m{}'.format(e))
prox = open('.Proxs.txt', 'r').read().splitlines()
def cc():
    while True:
############################        
        A1 = "1234567890"
        A2 = "1234567890"
        A3 = "1234567890"
        A4 = "1234567890"
        A5 = "1234567890"
        A6 = "1234567890"
        A6 = "1234567890"
        A7 = "1234567890"
############################      
        s1 = ''.join(random.choices(A1))
        s2 = ''.join(random.choices(A1))
        s3 = ''.join(random.choices(A1))
        s4 = ''.join(random.choices(A1))
        s5 = ''.join(random.choices(A1))
        s6 = ''.join(random.choices(A1))
        s7 = ''.join(random.choices(A1))
############################        
        a1 = "qwertyuiopasdfghjklzxcvbnm1234567890"
        a2 = "qwertyuiopasdfghjklzxcvbnm1234567890"
        a3 = "qwertyuiopasdfghjklzxcvbnm1234567890"
        a4 = "qwertyuiopasdfghjklzxcvbnm1234567890"
        a5 = "qwertyuiopasdfghjklzxcvbnm1234567890"
        a6 = "qwertyuiopasdfghjklzxcvbnm1234567890"
        a7 = "qwertyuiopasdfghjklzxcvbnm1234567890"
############################        
        v1 = ''.join(random.choices(a1))
        v2 = ''.join(random.choices(a1))
        v3 = ''.join(random.choices(a1))
        v4 = ''.join(random.choices(a1))
        v5 = ''.join(random.choices(a1))
        v6 = ''.join(random.choices(a1))
        v7 = ''.join(random.choices(a1))
############################        
        user1 = v1+'__'+v2+v3
        user2 = '_'+v1+v1+v5+v5
        user3 = '_'+v1+v1+v2+v2
        user4 = v1+v2+v1+'.'+v2     
        user5 = v1+v1+v2+v2+v3
        user6 = v1+v2+v2+'_'+v1
        user7 = v1+v2+v1+'_'+v1
        user8 = v1+v2+v1+v2+'_'
        user9 = '__'+v1+v2+v1
        user10 = '_'+'.'+v1+v6+v7
        user11 = v1+v2+v2+'.'+v1
        user12 = v1+'_'+v1+v3+v3
        user13 = v1+'_'+'.'+'_'+v2
        user14 = v6+'.'+v7+v5+v4
        user15 = v1+v2+'.'+v2+v1
        user16 = '__'+v1+v2+'_'
        user17 = v1+'_'+v2+'__'
        user18 = v1+'.'+v2+'.'+v3
        user19 = v1+'_'+v1+v2+v2
        user20 = '_'+v1+v2+v1+v1
        user21 = '_'+s1+s2+s3+s4
        user22 = s1+'_'+s2+s3+s4
        user23 = s1+s2+'_'+s3+s4
        user24 = s1+s2+s3+'_'+s4
        user25 = s1+s2+s3+s4+'_'
        user26 = s1+'.'+s2+s3+s4
        user27 = s1+s2+'.'+s3+s4
        user28 = s1+s2+s3+'. '+s4        
        user29 = '_'+s1+s1+s3+s4
        user30 = s1+'_'+s2+s2+s4
        user31 = s1+s2+'_'+s3+s3
        user32 = s1+s2+s3+'_'+s4
        user33 = s1+s1+s3+s4+'_'        
        user34 = v1+v2+v3+v3+v3
        user35 = v1+v1+v1+v2+v2
        user36 = v1+'_'+v2+'.'+v3
        user37 =  v1+'.'+v2+'_'+v3
        user38 = v1+'_'+v1+v1+v2
        user39 = v1+v1+v1+'_'+v2
        user40 = s1+'__'+v1+s1
        user41 = v1+v2+v1+v2+v1
        user42 = v1+'__.'+v2
        user43 = '__'+v1+v2+v1
        user44 = '_'+v1+v1+v2+'_'
        user45 = '_'+v1+'.'+v1+v2
        user46 = v1+s1+s1+s1+v1
        user47 = v1+'.'+s1+'__'
        user48 = v1+'._'+v1+'_'
        user49 = s1+s1+v1+v1+v1
        user50 = v1+'.'+s1+v1+'_'
############################        
        Rre =user1,user2,user3,user4,user5,user6,user7,user8,user9,user10,user11,user12,user13,user14,user15,user16,user17,user18,user19,user20,user21,user22,user23,user24,user25,user26,user27,user28,user29,user30,user31,user32,user33,user34,user35,user36,user37,user38,user39,user40,user41,user42,user43,user44,user45,user46,user47,user48,user49,user50
        user = ''.join(random.choices(Rre,k=1))
        url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'ar-US,ar;q=0.9,es-US;q=0.8,es;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/emailsignup/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(generate_user_agent()),
            'x-asbd-id': '129477',
            'x-csrftoken': 't7OXhwnoZOxph4oyq6Fuyd6ERG0tbyGz',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '1014458754',
            'x-requested-with': 'XMLHttpRequest',
        }
        
        data = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1719328029:jjfjxhgkgxytvyj',
            'email': 'zebz120zebz@gmail.com',
            'first_name': 'zebz',
            'username': f'{user}',
            'opt_into_one_tap': 'false',
        }
        
        re = requests.post(url, headers=headers, data=data).text
        if '"dryrun_passed":true' in re:
            print(f'{F} GOOD{B} → {F} {user}')
            RRT = f"""
 GOOD USER INSTAGRAM           
◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇

user → `{user}`

◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇      
      
            """
            RTR = """
تم تصيد يوزر انستا            
            """
            pop=[
"الشخص",f"tg://openmessage?user_id={id}",
            ]             
            pooo=[
"المطور",f"t.me/e_z_d",
            ]
            pazok.tele_ms(tokenzebz,idzebz,txt=RTR,buttons=pop)            
        else:
            print(f'{Z} Bad{B} → {Z} {user}', end='\r')    
Threads = []
for t in range(5):
    x = threading.Thread(target=cc)
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join()                        
