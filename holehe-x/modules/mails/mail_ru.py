# Holehe-X Module #
from localuseragent import useragents
from random import choice

async def mail_ru(email, client, out):
    name        = "mail_ru"
    domain      = "mail.ru"
    method      = "api"
    rate_limit  = False

    url = f"https://account.mail.ru/api/v1/user/password/restore?email={email}&htmlencoded=false"
    response = await client.get(url)
    data = response.json()

    if data["body"]["id"]:
        recovery_emails = data["body"]["emails"] if data["body"]["emails"] else []
        recovery_phones = data["body"]["phones"] if data["body"]["phones"] else []
        support_disabled = data["body"]["support_disabled"]

        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": True,
                    "exists": True,
                    "emailrecovery": recovery_emails,
                    "phoneNumber": recovery_phones,
                    "others": {'id': data["body"]["id"]}})
        return data
