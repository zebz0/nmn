import requests, random, threading, pazok
from user_agent import *
Z = '\033[1;31m'  # أحمر
F = '\033[2;32m'  # أخضر
e = "\u001b[38;5;242m" #رمادي داكن
m = "\u001b[38;5;15m" #ابيض
E = "\u001b[38;5;8m" #رمادي فاتح
Aa =0
Bb = 0
token = "6504402239:AAHkJsUdnbkPpeyHK1Jt-Zgps3rvAaGCju4"
id = 6060332252
logo = """

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⠛⠛⠛⠛⠛⠿⠶⢶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⠴⠾⣛⣛⣿⣭⣿⣿⣿⣋⣉⡙⠻⢷⣤⣄⣀⣀⣀⠀⠀⠀⠉⠙⠻⠦⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡀⠨⠭⠵⣶⣾⣿⢿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠙⣶⣵⣢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣤⠶⠚⠋⠙⢚⣛⣛⣿⡿⠿⢟⣿⡿⡟⢹⣿⡟⠛⠛⡿⣿⣿⣿⣶⠄⣀⣴⡿⢛⠉⣉⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠠⠾⠛⣒⣤⠶⠾⠿⠛⠛⠃⠀⠀⠀⠻⣿⣧⠡⡘⠿⡿⠞⣡⠃⢸⣿⣿⣿⡿⠟⡩⠞⠁⠀⠀⠈⠉⠙⠳⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣠⠴⠾⠿⢷⣶⣶⣶⣶⡶⠤⠤⠤⠤⠀⠀⠀⠀⠁⠈⠑⠒⠋⠡⣒⣛⡩⠞⢋⡠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣀⣤⣴⣒⣛⣛⠛⠛⠛⠛⠛⠒⠒⠂⠀⣀⣀⣤⡤⠤⠤⠀⣀⣤⠽⠛⣉⣤⣾⣯⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠉⠉⠉⠉⠉⣉⣭⠿⠃⠀⠀⠀⠀⠰⠶⠿⠭⣥⣤⣤⣶⣶⣿⣿⣿⡿⠿⠛⠛⠛⠛⠓⠊⠍⠙⠻⢶⣦⣄⡀⠀⠀⠀⠀⠀⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣀⣤⣖⣿⣭⡤⠶⢶⣶⣾⡿⠿⢿⣿⣻⠷⠂⢈⣽⣿⣿⣿⢟⣡⣤⣶⣾⠿⠿⠿⠿⠿⡿⠿⠷⠶⠽⣿⣿⣶⣄⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠋⠉⠉⠁⣀⣠⡤⠶⠛⠉⣠⣴⣾⠟⠋⣁⡤⠞⢛⣽⣿⣿⣿⣿⡿⠛⠉⡀⠀⠆⡄⡀⢢⣇⠀⠀⠀⠀⠀⠉⠛⢿⣦⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢶⣾⣛⣋⠉⠁⠀⣀⣴⡾⠟⠉⠀⠐⠈⠁⠀⢠⣾⣿⣿⣿⡿⠋⢠⡎⣴⣷⢰⢸⡇⢣⠀⠻⣗⠀⠀⠀⠀⠀⠀⠈⣿⢀⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠛⠛⠻⢿⡿⠋⠀⠀⠀⢀⠀⠀⠀⠀⡿⠁⢸⣿⡟⠁⢀⣿⡾⠃⠹⡿⢸⡇⠈⢧⠀⠙⢷⣄⠀⠀⠀⠀⠀⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡟⠁⢀⡠⠔⠈⠀⠀⠀⠀⢸⠁⠀⢸⣿⠁⠀⣾⡟⠀⠀⠀⠃⠈⡇⠀⠘⣧⠀⠈⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣷⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⡟⠀⢸⡟⠀⠀⣼⠀⠀⠀⠀⣀⠀⠸⣆⠀⠀⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⡿⣰⠁⠀⠀⠀⠀⠀⢠⠃⠀⢀⣿⡇⠀⠀⡿⠀⠀⣼⡏⠀⠀⠀⠀⣿⡄⠀⢿⡀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⡇⣿⢀⡎⠀⠀⠀⠠⣛⠀⠀⣸⣿⣿⠀⢰⠃⠀⣼⣿⠁⠀⡀⠀⣸⢿⡇⠀⢸⡇⠀⡿⢣⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢡⢿⣾⡇⠀⠀⢀⣴⣿⣷⠄⣿⠇⣿⠀⠈⢀⣾⣿⠇⣠⡾⠀⢠⡿⢸⡇⠀⢸⡇⡜⣴⣿⣿⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⢿⣇⠀⣰⡌⠻⡿⢃⣾⠏⠀⣿⠀⢀⣾⣻⡟⣰⣿⠃⢀⢺⠃⣼⡇⠀⣾⣿⡷⠈⠻⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣶⣿⠃⢰⡆⡼⠋⣀⣠⣭⣤⠸⠣⠟⠐⠛⣃⣠⡞⠈⢀⣿⠃⣰⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠀⢸⢃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣾⣟⣴⣿⠋⠀⠀⠀⠀⢀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣨⣾⡿⠛⢛⡋⣿⣿⣿⡿⠿⠿⢛⣫⠄⠀⣼⣿⡿⠟⠁⠀⢀⣀⣤⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠠⣤⣶⣶⣿⣿⣿⣿⣿⠏⠀⢀⡿⠃⣰⣶⠖⠀⠼⠗⢛⣁⣀⡜⠟⣉⣤⣴⣶⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠁⠀⠀⠉⠀⢠⣶⣅⠀⢀⣾⣿⣿⣿⡟⠀⠘⠛⠛⠛⠿⠟⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣿⣿⠟⠁⠞⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
print(logo)
def cc():
    while True:
        global Aa, Bb
        lists=[]        
        uu = "qwertyuioplkjhgfdsamnbvcxz1234567890"
        a="".join(random.choice(uu))
        b="".join(random.choice(uu))
        c="".join(random.choice(uu))
        d="".join(random.choice(c))
        e="".join(random.choice(d))
        user1 = '_'+a+a+b+b
        user2 = a+'_'+a+b+b
        user3 = a+a+'_'+b+c
        user4 = a+a+b+'_'+b
        us = user1,user2,user3,user4
        user="".join(random.choice(us))

        def gen():
            import random
            user=''.join(random.choice('12')for i in range(2))
            if user in lists:
                return gen()
            else:
                lists.append(user)
                return user
        #user = "djsvsj_76h"
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
            'x-csrftoken': 'uBfsWtwDTXF4HPrDRO1Emh5rk0oggwpK',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '1015175619',
            'x-requested-with': 'XMLHttpRequest',
        }
        
        data = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1722002107:sjbeejshe',
            'email': 'zebz120zebz@gmail.com',
            'first_name': 'zebz',
            'username': user,
            'client_id': '16gv3b81s0f9rf1jol29ph9pso91i1s38x16a8il51ar301z14a445p',
            'seamless_login_enabled': '1',
            'opt_into_one_tap': 'false',
        }
        
        re = requests.post(url, headers=headers, data=data).text
        if '"dryrun_passed":true' in re:
            Aa +=1
            print(f' {E}[ {Aa} ] {F} GOOD USER : {E} {user}')
            RRT = f"""    

user → `{user}`
        
            """            
                        
            pooo=[
"زيــبز",f"t.me/e_z_d",
"شــاهـين",f"t.me/ShahenSaD", 
            ]
            pazok.tele_ms(token,id,txt=RRT,buttons=pooo)      
        elif '"spam":true' in re:
              print('VPN')               
        else:
            Bb +=1
            print(f' {E}[ {Bb} ] {Z} BAD USER : {E} {user}', end='\r')
Threads = []
for t in range(5):
    x = threading.Thread(target=cc)
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join()                        
        
            
