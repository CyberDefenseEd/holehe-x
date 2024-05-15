# Holehe-X Module #
from localuseragent import useragents
from random import choice


async def vsco(email, client, out):
    name="vsco"
    domain = "vsco.co"
    method = "register"
    rate_limit=False

    headers = {
        'Authorization': 'Bearer 7356455548d0a1d886db010883388d08be84d0c9',
    }

    try:
        r = await client.get(f'https://api.vsco.co/2.0/users/email?email={email}', headers=headers)
        resp=r.json()
        if resp["email_status"]=="has_account":
            out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                        "rateLimit": False,
                        "exists": True,
                        "emailrecovery": None,
                        "phoneNumber": None,
                        "others": None})
        elif resp["email_status"]=="no_account":
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
    except Exception:
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": True,
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
