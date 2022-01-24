import requests, random, httpx, os, time

global infotoken

infotoken = 'https://discord.com/api/v9/users/@me'

thebios = []

cookiemonster = httpx.get('https://discord.com/register').headers['set-cookie']
sep = cookiemonster.split(";")
sx = sep[0]
sx2 = sx.split("=")
dfc = sx2[1]
split = sep[6]
split2 = split.split(",")
split3 = split2[1]
split4 = split3.split("=")
sdc = split4[1]

with open('messages.txt','r', encoding='utf-8') as bios:
    for line in bios:
        thebios.append(line)

def getBio():
    return random.choice(thebios)

def headers(tokan):
    header = {
        "authority": "discord.com",
        "method": "POST",
        "path": "/api/v9/users/@me",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US",
        "Authorization": f"{tokan}",
        "content-length": "0",
        "cookie": f'__dcfduid={dfc}; __sdcfduid={sdc}',
        "origin": "https://discord.com",
        'referer': 'https://discord.com/channels/@me',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": 'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0',
        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }
    return header

while True:
    os.system('cls' if os.name=='nt' else 'clear')
    global tukan
    tukan = input('Token: ')
    r = requests.get('https://discordapp.com/api/v9/users/@me/library', headers = headers(tukan))
    if r.status_code != 200:
        print('Invalid Token')
        time.sleep(5)
    else:
        break

def login():
    reqinfo = requests.get(infotoken, headers=headers(tukan))

    return f'{reqinfo.json()["username"]}#{reqinfo.json()["discriminator"]}'

def main(delay):
    statusurl = 'https://discord.com/api/v9/users/@me/settings'
    os.system('cls' if os.name=='nt' else 'clear')
    print(f'Logged In As {login()}')
    os.system('pause')
    while True:
        payload = {
            'custom_status': {'text': getBio()}
        }

        applybio = requests.patch(statusurl, headers=headers(tukan), json=payload)
        time.sleep(delay)

delay1 = float(input('Delay: '))

if __name__ == '__main__':
    main(delay1)
