import os, requests, time, threading, random

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
logo = """\u001b[38;5;8m \x1b[1m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⢿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⠀⠙⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣤⣀⠀⠀⢿⣿⣿⠇⠀⢹⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⢀⣴⣿⣿⡿⠿⠿⠿⣿⣿⣷⣦⠀⠈⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⢀⣾⣿⡿⠉⠀⠀⠀⠀⠀⠙⢿⣿⣷⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⢸⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡇⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⢸⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡇⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡇⠀⠀⠀⠀⢿⣿⣷⣄⡀⠀⠀⠀⢀⣠⣿⣿⡟⠀⠀⠀⢀⠘⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣷⣄⠙⠇⠀⠀⠀⠀⠀⠙⢿⣿⣿⣷⣶⣾⣿⣿⡿⠋⠀⠀⠀⣠⣿⣷⣄⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡿⢁⣆⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠉⠁⠀⠀⠀⠀⠘⢿⣿⡿⢃⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠰⠿⠿⠂⠀⠀⠀⠀⠀⠀⠀⠀⣠⡗⠀⠀⠀⠀⠀⠀⠀⠀⢀⣉⣠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣾⣿⣿⣧⣤⣤⣤⣴⣶⣾⣿⠃⣤⣤⣤⣤⣤⣤⣴⣶⣿⡿⢁⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠼⠿⠿⠿⠿⠿⠿⠿⠛⣉⣴⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣀⣀⣤⣤⣶⣶⣾⣿⡿⠋⠉⠀⠻⠿⠿⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠛⠿⢿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⢀⣀⠀⠀⢀⣤⣴⣶⣾⣿⢃⣶⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⣰⣿⣿⣷⢀⣾⣿⣿⣿⡿⠃⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⡿⠁⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
print(logo)
#====لوكو====
token = input(f' {E} Enter The {B}Token :{E} ')
id = input(f' {E} Enter The {B}ID :{E} ')
os.system('clear')
Aa = 0
Bb = 0
def cc():
    while True:
        global a, Aa, Bb
        u = pazok.user_ran('1')
        s = pazok.user_ran('1')
        e = pazok.user_ran('1')
        ue = u+'_'+e+'_'+s
        us = s+'.'+e+'.'+u
        uuu = ue, ue
        
        user = ''.join(random.choices(uuu)) 
    
    
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
                'x-csrftoken': 'NupVSsk8juLhrFuFhkn3w42vJdmpquV3',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': '0',
                'x-instagram-ajax': '1015662679',
                'x-requested-with': 'XMLHttpRequest',
            }
    
        tim = str(time.time()).split('.')[1]
        data = {
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:djdvdjdhdjx',
                'email': 'zebz120zebz@gmail.com',
                'first_name': 'zebz',
                'username': f'{user}',
                'client_id': 'e3mnyt1qvnquo1gdujdd118kii31fjhqzt9jgs8g1nsxc051157yny',
                'seamless_login_enabled': '1',
                'opt_into_one_tap': 'false',
            }
    
        re = requests.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/', headers=headers, data=data).text
        if '"dryrun_passed":true' in re:
                Aa += 1
                print(f'{F} [ {Aa} ] GOOD USER insta : {user} ')
                RRT = f"""
 GOOD USER INSTAGRAM           
◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇

user → `{user}`

◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇      
      
            """            
                        
                pooo=[
"المطور",f"t.me/p_sps",
            ]
                pazok.tele_ms(token,id,txt=RRT,buttons=pooo)       
        elif '"spam":true' in re:
                print('VPN')
        else:
                Bb += 1
                print(f'{Z} [ {Bb} ] BAD USER insta : {user} ')
Threads = []
for t in range(5):
    x = threading.Thread(target=cc)
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join()                
