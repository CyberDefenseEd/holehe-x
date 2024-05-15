# Holehe-X Module #
from localuseragent import useragents
from random import choice


async def replit(email, client, out):
    name = "replit"
    domain = "replit.com"
    method = "register"
    rate_limit=True

    headers = {
        'User-Agent': choice(useragents["browsers"]["firefox"]),
        'Accept': 'application/json',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'content-type': 'application/json',
        'x-requested-with': 'XMLHttpRequest',
        'Origin': 'https://replit.com',
        'Connection': 'keep-alive',
    }

    data = '{"email":"' + str(email) + '"}'

    response = await client.post('https://replit.com/data/user/exists', headers=headers, data=data)
    try:
        if response.json()['exists']:
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
    except Exception:
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})