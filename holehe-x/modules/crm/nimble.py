# Holehe-X Module #
from localuseragent import useragents
from random import choice


async def nimble(email, client, out):
    name = "nimble"
    domain = "nimble.com"
    method= "register"
    rate_limit=False

    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': choice(useragents["browsers"]["chrome"]),
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.nimble.com/',
        'Accept-Language': 'en-US;q=0.8,en;q=0.7',
    }

    response = await client.get('https://www.nimble.com/lib/register.php?email='+email, headers=headers)

    if response.text=='"I thought you looked familiar! This email is already registered."':
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": False,
                    "exists": True,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
    elif response.text=="true":
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": False,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
    else:
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
    return()
