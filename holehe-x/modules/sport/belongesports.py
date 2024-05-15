# Holehe-X Module #
from localuseragent import useragents
from random import choice

async def belongesports(email, client, out):
    name        = "belongesports"
    domain      = "belongesports.gg"
    method      = "register"
    rate_limit = False

    try:

        headers = {"User-Agent": choice(useragents["browsers"]["chrome"])}

        req = await client.get("https://www.belongesports.gg/signup/email/check/"+email, headers=headers)


        if '{"email_taken" : {"status" : "true"}}' == req.text:
            out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                        "rateLimit": False,
                        "exists": True,
                        "emailrecovery": None,
                        "phoneNumber": None,
                        "others": None})


        elif '{"email_taken" : {"status" : "false"}}' == req.text:
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

    except :
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})