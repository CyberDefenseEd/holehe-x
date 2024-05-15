# Holehe-X Module #
from localuseragent import useragents
from random import choice


async def komoot(email, client, out):
    name = "komoot"
    domain = "komoot.com"
    method= "register"
    rate_limit=True

    headers = {
        'User-Agent': choice(useragents["browsers"]["firefox"]),
        'Accept': '*/*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/json',
        'Origin': 'https://account.komoot.com',
        'Connection': 'keep-alive',
        'Referer': 'https://account.komoot.com/signin',
    }

    data = '{"email":"'+email+'"}'

    try:
        response = await client.post('https://account.komoot.com/v1/signin',headers=headers,data=data)
        if 'login' in response.json()['type']:
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
