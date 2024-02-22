import os
import sys
import subprocess
import webbrowser
import time
import requests
import random
import threading
import datetime

Z = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
C = '\x1b[1;97m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
G = '\x1b[1;32m'
M = '\x1b[0;35m'
R = '\x1b[0;31m'
W = '\x1b[0;37m'
V = '\x1b[0;35m'
O = '\x1b[0;33m'
P = '\x1b[0;95m'
U = '\x1b[0;94m'
p = '\x1b[1m'
o = '\x1b[3m'
j = '\x1b[4m'
k = '\x1b[7m'
g = '\x1b[0m'
print (X+"═━═━═━═━═━━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━━═━═━═━═━═━═━━═━═━═━═━━═━═━═━═━═━═━━═━═━═━═━━═━═━═━═━═━═━")
def printt(word, delay=1):
    for letter in word:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
zebz=j+"""
                              ..      ...   . . .....       
                                       ...       ....       
                                      .....   .  ..... .    
           .   .     . .               . ..       . .       
          .......      ..                                   
    .. ......        .    .....  ..... ..:.                 
                                  .... ......               
                                                            
                  . ....                                    
            .  .:::::^:^:^:.:..                             
.          .::^^^^^~^~~~^~^~~^~~~^:..:...:...               
         .:^^^^~!!!!!!~!!!!~~~!!!~~::^^^:^:^:.:.:           
      ...:^:~~~!!!!!!!!!!!!!!!!!!~~^~!~~~~^^^::::. .        
    .::^:^^^~~~!~~~~~~!~!~!~~!~!~!!!!~!~!~~~~~^^:.:.:       
   ..:^~^^~~~~~~~~~~~~!~~~~~~~~!~~~~~~!~~~~~~~~~^^:...      
   ...:~~^~!!!!!!!!!!~!~!!!!!!~!!!!!!!!~!!!!!!~^~~. .       
   ..:.:~~^~~~!~!~!!!!!!!!!!~!!!!!!!!!!!!!!!!~^~!^..:.      
    ..  .^::^:~~~~~!!!!!!!~^^^~~~~~!!!!!~~~^:^^~~. ....     
     .   ^:^^~!!!~~~~~~~!~~^~~~~!!~~~~!~!~~~^^^~^  ....     
        .~!~~~~~~~~^:^:^^^~~~~~!~~~:^^~~~~~~~~~~^   ::.     
       .:~~~~^^^::.. ....^^~!!~^~^:::::^^^^~~~!!~^  .::     
        .::.             .::~~~:^..        ...^^^:.  .      
      .^.                ..:^^^:^:.             ::.         
      :~        ...    . .:~!!~~^:       .  ..   ^^         
      :~   ..:^:::...  .:^~::::^~~:.    .::.     :^:        
     .:~^:...^~^^::^::.^!~.    .^~~^:..:.:^^:.  .:~:.       
    .~^:^~^^^^^:~~~~^^^!!:      .^^^^~^^^^:::.::^^^^.       
 .:^~!!!:::::^^^!!~^::^~:        .^::^^~^!~^^~^^^:~!^..     
  ...^^::.    ..:^~~^:^.          .^^~!~^^.. ..:^~!~^::.    
     .:: .:.. ....^~~^^.           ^~~~^:....:..^^~:        
          ..:.:::::~~^~:    .^.   :~^~^....^:::.:::         
              .::::^!~~~^:::~^::::~^!~^:.:^:..    .       ..
          .:.   .:^^:^^^~^:::.^^^^~^^~~^:.  ..              
          .::.   . .:~::^::^: ^:.:..:: .   .:.         ...  
           .~^.    :~~:~~^^~~:!~^~^^!: . ..~^.        ...   
            :~^.   ..::^:::^^.^:::::^.   .^~:          . .. 
            .^~~~:...:~~^~:^~:~:~~^^.    ^!^.          . .  
            ..:~!^~~^^:::^:::.:.^::^:~~~~~^:.       .. .    
            ....^~!~^^.::::^^^^::^^:^!~~^^...       .       
 .          .. .:~~!~~^~~~^^~~~~^^^^~!!~~: ..       ...     
  .             ..^~^^!~~~~~!~~!~!~~~~~^.. ..       :...    
                  .^~~~~~~~~~~~~~~~^^~::           ....     
                    ..:^^:::~:^:^^^^:.            .....     
                                                            
     .                                                   . .
                                                  ...   .^..
       .    .                               ....:.:..  . .  
   .   ..  ...  .                          .. .   .   .:.. .
"""
printt(zebz, delay=0.001)
print (X+"═━═━═━═━═━━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━━═━═━═━═━═━═━━═━═━═━═━━═━═━═━═━═━═━━═━═━═━═━━═━═━═━═━═━═━")
token = input(p + f''' {C}[ {F}➠ {C}] {O}TOKEN  {F}: {k}''')
print (X+"═━═━═━═━═━━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━━═━═━═━═━═━═━━═━═━═━═━━═━═━═━═━═━═━━═━═━═━═━━═━═━═━═━═━═━")
id = input(p + f''' {C}[ {F}➠ {C}] {O}ID {F}: {k}''')
os.system('clear')

def loading_animation():
    animation = [
        '[■□□□□□□□□□]',
        '[■■□□□□□□□□]',
        '[■■■□□□□□□□]',
        '[■■■■□□□□□□]',
        '[■■■■■□□□□□]',
        '[■■■■■■□□□□]',
        '[■■■■■■■□□□]',
        '[■■■■■■■■□□]',
        '[■■■■■■■■■□]',
        '[■■■■■■■■■■]']
    num_iterations = 2
    counter = 0
    for i in range(40):
        color_code = random.randint(91, 96)
        colored_animation = animation[i % len(animation)].replace('■', f'''\x1b[1;{color_code}m■\x1b[0m''')
        sys.stdout.write(p + '\r- Loading  ' + colored_animation)
        sys.stdout.flush()
        time.sleep(0.1)
    counter += 1
    if counter >= num_iterations:
        pass

    

loading_animation()
os.system('clear')
insta = '1234567890qwertyuiopasdf._ghjklzxcvbnm'
ajw = '_'
agents = ['Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36','Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36']
def instaa(user, agent):
    url = requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/', headers={
        'Host': 'www.instagram.com',
        'content-length': '85',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'sec-ch-ua-mobile': '?0',
        'x-instagram-ajax': '81f3a3c9dfe2',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'x-requested-with': 'XMLHttpRequest',
        'x-asbd-id': '198387',
        'user-agent': agent,
        'x-csrftoken': 'jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv',
        'sec-ch-ua-platform': '"Linux"',
        'origin': 'https://www.instagram.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.instagram.com/accounts/emailsignup/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-IQ,en;q=0.9',
        'cookie': 'csrftoken=jzhjt4G11O37lW1aDFyFmy1K0yIEN9Qv; mid=YtsQ1gABAAEszHB5wT9VqccwQIUL; ig_did=227CCCC2-3675-4A04-8DA5-BA3195B46425; ig_nrcb=1' },
        data=f'email=aakmnnsjskksmsnsn%40gmail.com&username={user}&first_name=&opt_into_one_tap=false')
    if '{"message":"feedback_required","spam":true,"feedback_title":"Try Again Later","feedback_message":"We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.","feedback_url":"repute/report_problem/scraping/","feedback_appeal_label":"Tell us","feedback_ignore_label":"OK","feedback_action":"report_problem","status":"fail"}' in url.text:
        print(o + f'''  ❌ ➠ {C}[ {Z}{user} {C}]''')
    elif '"errors": {"username":' in url.text or '"code": "username_is_taken"' in url.text:
        print(o + f'''  ❌ ➠ {C}[ {Z}{user} {C}]''')
        
        
    else:
        email = 0
        print(F + f'''  ✅ ➠ {C}[ {F}{user} {C}]''')
        email += 1
        god = f'''\n\n- - - - - 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 - - - - -\n\n{user}\n\n- - - - - @U_J_3 - - - - - -\n\n'''
        requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={god}''')

def generate_special_username():
    litters = '1234567890abcdefghijklmnopqstuwxyz'
    num_letters = random.choice([2, 3, 3, 3, 3, 4, 4, 4, 3, 2, 4, 3])
    num_underscores = 5 - num_letters
    positions = random.sample(range(5), num_letters)
    username = ''
    for i in range(3):
        if i in positions:
            username += random.choice(litters)
        username += '_'
    return username

def users():
    counter = 0
    while True:
        username = generate_special_username()
        agent = random.choice(agents)
        instaa(username, agent)
        counter += 1
        if counter % 3 == 0:
            time.sleep(10)

num_threads = 20
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=users)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()