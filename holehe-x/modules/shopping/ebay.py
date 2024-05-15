# Holehe-X Module #
from localuseragent import useragents
from random import choice

async def ebay(email, client, out):
    name        = "ebay"
    domain      = "ebay.com"
    method      = "login"
    rate_limit = True

    headers = {
        'User-Agent': choice(useragents["browsers"]["chrome"]),
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'https://www.ebay.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }
    try:
        req = await client.get(
            "https://www.ebay.com/signin/", headers=headers)
        srt = req.text.split('"csrfAjaxToken":"')[1].split('"')[0]
    except IndexError:
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
        return None

    data = {
        'identifier': email,
        'srt': srt
    }

    req = await client.post(
        'https://signin.ebay.com/signin/srv/identifer',
        data=data, headers=headers)
    results = json.loads(req.text)
    if "errorMsg" in results.keys():
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": False,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
    else:
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": False,
                    "exists": True,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
