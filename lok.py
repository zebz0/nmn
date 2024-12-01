import requests
import pazok
import threading
import random
import time

token = "7401317564:AAHyOTTDBREFwV1s4aJ-tL5cTr1RksIJuKo"  # توكنك
id = 2121855589  # ايديك ↑

def cc(): 
    while True:
        b = '_.'
        a = "qwertyuioplkjhgfdsamnbvcxz1234567890"
        u = ''.join(random.choices(a))
        s = ''.join(random.choices(a))
        e = ''.join(random.choices(a))
        r = ''.join(random.choices(b))
        U = r + e + s + u
        S = e + r + s + u
        E = e + s + r + u
        R = e + s + u + '_'
        T = u+s+e+r
        USER = [U, S, E, R]
        user = ''.join(random.choices(USER))
        
        # التحقق من أن اسم المستخدم لا ينتهي بنقطة
        if user.endswith('.'):
            continue
        
        headers = {'user-agent': pazok.agnt()}
        
        try:
            re = requests.get(f"https://www.tiktok.com/@{user}", headers=headers).text
            
            if '"statusCode":10221' in re:
                print(f'GOOD USER : {user}')
                RRT = f"""
                user → `{user}`
                """
                
                pooo = [
                    "المطور", f"t.me/justboy",
                    "فحص", f"https://www.tiktok.com/@{user}?",
                ]
                pazok.tele_ms(token, id, txt=RRT, buttons=pooo)
                
            elif '"statusCode":10222' in re:
                print(f'BAD USER : {user}')
                
            else:
                print(f'error USER : {user}')
                
        except requests.RequestException as e:
            time.sleep(70)
            print(' النت ضعيف')

Threads = []
for t in range(10):
    x = threading.Thread(target=cc)
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join()
