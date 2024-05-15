# Holehe-X Module #
from localuseragent import useragents
from random import choice


async def twitter(email, client, out):
    name = "twitter"
    domain = "twitter.com"
    method = "register"
    rate_limit=False

    try:
        req = await client.get(
            "https://api.twitter.com/i/users/email_available.json",
            params={
                "email": email})
        if req.json()["taken"]:
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
