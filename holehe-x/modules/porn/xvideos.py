# Holehe-X Module #
from localuseragent import useragents
from random import choice


async def xvideos(email, client, out):
    name = "xvideos"
    domain = "xvideos.com"
    method= "register"
    rate_limit=False

    headers = {
        'User-Agent': choice(useragents["browsers"]["firefox"]),
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'https://www.xvideos.com/',
    }

    params = {
        'email': email,
    }
    try:
        response = await client.get('https://www.xvideos.com/account/checkemail', headers=headers, params=params)
    except Exception:
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
        return()
    try:
        if response.json()['result'] == False and "This email is already in use or its owner has excluded it from our website" in response.text:
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
