# Holehe-X Module #
from localuseragent import useragents
from random import choice


async def armurerieauxerre(email, client, out):
    name = "armurerieauxerre"
    domain = "armurerie-auxerre.com"
    method = "register"
    rate_limit=False

    headers = {
        'User-Agent': choice(useragents["browsers"]["chrome"]),
        'Accept': '*/*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.armurerie-auxerre.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }

    data = {
        'mail': email
    }

    req = await client.post('https://www.armurerie-auxerre.com/customer/Email/email/', headers=headers, data=data)
    if req.text == "exist":
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
