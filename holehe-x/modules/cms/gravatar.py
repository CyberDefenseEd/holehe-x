# Holehe-X Module #
from localuseragent import useragents
from random import choice


async def gravatar(email, client, out):
    name = "gravatar"
    domain = "en.gravatar.com"
    method="other"
    rate_limit=False

    hashed_name = hashlib.md5(email.encode()).hexdigest()
    r = await client.get(f'https://en.gravatar.com/{hashed_name}.json')
    if r.status_code != 200:
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": False,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
        return None
    else:
        try:
            data = r.json()
            FullName = data['entry'][0]['displayName']

            others = {
                'FullName': str(FullName),
                'ProfileId': str(data['entry'][0]["profileUrl"])
            }

            out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                        "rateLimit": False,
                        "exists": True,
                        "emailrecovery": None,
                        "phoneNumber": None,
                        "others": others})
            return None
        except Exception:
            out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                        "rateLimit": True,
                        "exists": False,
                        "emailrecovery": None,
                        "phoneNumber": None,
                        "others": None})
            return None