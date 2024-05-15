# Holehe-X Module #
from localuseragent import useragents
from random import choice


async def caringbridge(email, client, out):
    name = "caringbridge"
    domain = "caringbridge.org"
    method= "register"
    rate_limit=False

    cookies = {
        'lang': 'en_US',
        'showSurvey': 'true',
        'cookiesEnabled': 'true',
    }

    headers = {
        'User-Agent': choice(useragents["browsers"]["chrome"]),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en,en-US;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.caringbridge.org',
        'Connection': 'keep-alive',
        'Referer': 'https://www.caringbridge.org/signin',
        'Sec-GPC': '1',
        'TE': 'Trailers',
    }

    data = {
        'csrf': '',
        'email': email,
        'password_placeholder': '',
        'submit-btn': 'Continue'
    }
    try:
        response = await client.post('https://www.caringbridge.org/signin', headers=headers, cookies=cookies, data=data, timeout=3)
    except Exception:
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
        return()
    if "Welcome Back," in response.text:
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
