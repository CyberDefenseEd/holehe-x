# Holehe-X Module #
from localuseragent import useragents
from random import choice


async def instagram(email, client, out):
    name = "instagram"
    domain = "instagram.com"
    method = "register"
    rate_limit=True

    headers = {
        'User-Agent': choice(useragents["browsers"]["chrome"]),
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'https://www.instagram.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

    try:
        freq = await client.get("https://www.instagram.com/accounts/emailsignup/", headers=headers)
        token = freq.text.split('{\\"config\\":{\\"csrf_token\\":\\"')[1].split('\\"')[0]
    except Exception:
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
        return None

    data = {
        'email': email,
        'username': ''.join(choice(string.ascii_lowercase + string.digits) for i in range(random.randint(6, 30))),
        'first_name': '',
        'opt_into_one_tap': 'false'
    }
    headers["x-csrftoken"] = token
    check = await client.post(
        "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/",
        data=data,
        headers=headers)
    check = check.json()
    if check["status"] != "fail":
        if 'email' in check["errors"].keys():
            if check["errors"]["email"][0]["code"] == "email_is_taken":
                out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                            "rateLimit": False,
                            "exists": True,
                            "emailrecovery": None,
                            "phoneNumber": None,
                            "others": None})
            elif "email_sharing_limit" in str(check["errors"]):
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
    else:
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
