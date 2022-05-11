import requests

usernames = open('usernames.txt', 'r').read().splitlines()

for username in usernames:
    try:
        r = requests.get(f'https://www.roblox.com/user.aspx?username={username}').url
        if 'www.roblox.com/users/' not in r: continue
        userid = r.split('/')[-2]
        r = requests.get(f'https://rblx.trade/api/v2/users/{userid}/inventory').json()
        if 'success' in r and r['error']['code'] == 'PrivateInventory':
            with open('rap.txt', 'a') as f:
                f.writelines(f'{username}:Private\n')
        else:
            with open('rap.txt', 'a') as f:
                f.writelines(f'{username}:{r["rap"]}:{r["value"]}\n')
        print(username)
    except Exception as e:
        print(e)
        usernames.append(username)

input('Done.')