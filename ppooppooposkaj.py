import os
import requests
import time
import threading
import random

try:
    import pazok
except:
    os.system('pip install pazok')

#==== الوان ====
Z = '\033[1;31m'  # أحمر
X = '\033[1;33m'  # أصفر
F = '\033[2;32m'  # أخضر
C = "\033[1;97m"  # أبيض
B = '\033[2;36m'  # أزرق
Y = '\033[1;34m'  # أزرق داكن
W = '\033[0;37m'  # رمادي
e = "\u001b[38;5;242m" # رمادي داكن
m = "\u001b[38;5;15m" # أبيض
E = "\u001b[38;5;8m"  # رمادي فاتح
p = '\x1b[1m'  # عريض
sf = '\x1b[38;5;190m' #اصفر
pr = '\x1b[38;5;208m' #برتقالي
B = '\033[2;36m'  # سماوي
E = "\u001b[38;5;8m" #رمادي فاتح

token = input(f'{sf} Enter Your {pr}Token : {sf} ')
id =input(f'{sf} EnteR Your {pr}Id : {sf} ')
os.system('clear')


Aa = 0
Bb = 0
def cc():
    global Aa, Bb
    while True:
        import random
        u = pazok.user_ran('1')
        s = pazok.user_ran('3')
        e = pazok.user_ran('1')
        w = pazok.user_ran('1')
        RT = pazok.user_ran('4')
        
        ue = '_' + w + u + u + w 
        us = w  + u + u + w + '_'
        uu = w + u + u + u + '_'
        ui = '_'+ w + u + u + u
        y = w + s + u + u + u
        o = w + s + u + u + w 
        I = u+'.'+e+'.'+w
        uuu = I, I
        user = ''.join(random.choices(uuu))
        #user = "44djshsih1_8"
        #user = "y_8_8"
        #user = pazok.user_file("username.txt", True)
        
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
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-csrftoken': 'ytgAvZRmGBmuNAcC9OTOr7N4PeOmyp1v',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1016981577',
    'x-requested-with': 'XMLHttpRequest',
}

        data = {
    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1727854499:ghjgcghfxg',
    'email': 'zebz120zebz@gmail.com',
    'first_name': 'zebz',
    'username': user,
    'client_id': 'Zt6i7gABAAFIGL1bi4PB-M-S2bUz',
    'seamless_login_enabled': '1',
    'opt_into_one_tap': 'false',
    'use_new_suggested_user_name': 'true',
}

        try:
            re = requests.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/', headers=headers, data=data).text
            
            if '"dryrun_passed":true' in re:
                Aa += 1
                print(f'{F} [ {Aa} ] GOOD USER insta : {user} ')
                RRT = f"GOOD USER INSTAGRAM\n\nuser → `{user}`\n"
                pooo = ["المطور", f"t.me/p_sps"]
                pazok.tele_ms(token, id, txt=RRT, buttons=pooo)
            elif '"spam":true' in re:
                print('VPN', end='\r')
            else:
                Bb += 1
                print(f'{Z} [ {Bb} ] BAD USER insta : {user} ', end='\r')
        except requests.RequestException as e:
            print(f"Communication is weak ")
            time.sleep(40)

Threads = []
for t in range(15):
    x = threading.Thread(target=cc)
    x.start()
    Threads.append(x)

for Th in Threads:
    Th.join()
