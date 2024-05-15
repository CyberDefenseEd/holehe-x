# Holehe-X Module #
from localuseragent import useragents
from random import choice


async def devrant(email, client, out):
    name = "devrant"
    domain = "devrant.com"
    method = "register"
    rate_limit=False

    headers = {
        'User-Agent': choice(useragents["browsers"]["chrome"]),
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://devrant.com',
        'Connection': 'keep-alive',
        'Referer': 'https://devrant.com/feed/top/month?login=1',
    }

    data = {
        'app': '3',
        'type': '1',
        'email': email,
        'username': '',
        'password': '',
        'guid': '',
        'plat': '3',
        'sid': '',
        'seid': ''
    }
    try:
        response = await client.post('https://devrant.com/api/users', headers=headers, data=data)
    except Exception:
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
        return None
    result = response.json()['error']
    if result == 'The email specified is already registered to an account.':
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": False,
                    "exists": True,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
    else:
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": False,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
