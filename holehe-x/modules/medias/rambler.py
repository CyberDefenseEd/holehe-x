# Holehe-X Module #
from localuseragent import useragents
from random import choice


async def rambler(email, client, out):
    name = "rambler"
    domain = "rambler.ru"
    method= "register"
    rate_limit=False

    headers = {
        'User-Agent': choice(useragents["browsers"]["firefox"]),
        'Accept': '*/*',
        'Accept-Language': 'en,en-US;q=0.5',
        'Referer': 'https://id.rambler.ru/champ/registration',
        'Content-Type': 'application/json',
        'Origin': 'https://id.rambler.ru',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

    data = '{"method":"Rambler::Id::get_email_account_info","params":[{"email":"' + email + '"}],"rpc":"2.0"}'

    response = await client.post(
        'https://id.rambler.ru/jsonrpc',
        headers=headers,
        data=data)
    try:
        if response.json()["result"]["exists"] == 0:
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
    except Exception:
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
