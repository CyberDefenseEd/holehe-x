# Holehe-X Module #
from localuseragent import useragents
from random import choice

async def deezer(email, client, out):
    name = "deezer"
    domain = "deezer.com"
    method = "register"
    rate_limit=False

    getAuth = await client.post('https://www.deezer.com/ajax/gw-light.php?method=deezer.getUserData&input=3&api_version=1.0&api_token=')
    jsonAuth = getAuth.json()

    payload = '{"EMAIL":"' + email + '"}'

    getAvailability = await client.post('https://www.deezer.com/ajax/gw-light.php?method=deezer.emailCheck&input=3&api_version=1.0&api_token={token}'.format(
        token = jsonAuth['results']["checkForm"]
    ), 
    data=payload)

    jsonAvailability = getAvailability.json()

    if jsonAvailability['results']['availability'] == False:
        out.append({
            "name" : name, "domain":domain, "method":method, "rate_limit":rate_limit,
            "rateLimit": False,
            "exists": True,
            "emailrecovery": None,
            "phoneNumber": None,
            "others":None
        })
    else:
        out.append({
            "name" : name, "domain":domain, "method":method, "rate_limit":rate_limit,
            "rateLimit": False,
            "exists": False,
            "emailrecovery": None,
            "phoneNumber": None,
            "others":None
        })