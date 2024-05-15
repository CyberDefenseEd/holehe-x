# Holehe-X Module #
from localuseragent import useragents
from random import choice


async def nike(email, client, out):
    name = "nike"
    domain = "nike.com"
    method = "register"
    rate_limit=False

    headers = {
        'User-Agent': choice(useragents["browsers"]["firefox"]),
        'Accept': '*/*',
        'Accept-Language': 'en,en-US;q=0.5',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Origin': 'https://www.nike.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.nike.com/',
        'TE': 'Trailers',
    }

    params = {
        'appVersion': '831',
        'experienceVersion': '831',
        'uxid': 'com.nike.commerce.nikedotcom.web',
        'locale': 'fr_FR',
        'backendEnvironment': 'identity',
        'browser': '',
        'mobile': 'false',
        'native': 'false',
        'visit': '1',
    }

    data = '{"emailAddress":"' + email + '"}'
    try:
        response = await client.post(
            'https://unite.nike.com/account/email/v1',
            headers=headers,
            params=params,
            data=data)
        if response.status_code == 409:
            out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                        "rateLimit": False,
                        "exists": True,
                        "emailrecovery": None,
                        "phoneNumber": None,
                        "others": None})
        elif response.status_code == 204:
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
    except Exception:
            out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                        "rateLimit": True,
                        "exists": False,
                        "emailrecovery": None,
                        "phoneNumber": None,
                        "others": None})
