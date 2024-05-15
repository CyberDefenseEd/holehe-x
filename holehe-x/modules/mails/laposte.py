# Holehe-X Module #
from localuseragent import useragents
from random import choice


async def laposte(email, client, out):
    name = "laposte"
    domain = "laposte.fr"
    method= "register"
    rate_limit=False

    headers = {
        'Origin': 'https://www.laposte.fr',
        'User-Agent': choice(useragents["browsers"]["chrome"]),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'https://www.laposte.fr/authentification',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    data = {
        'email': email,
        'customerId': '',
        'tunnelSteps': ''
    }
    try:
        response = await client.post('https://www.laposte.fr/authentification', headers=headers, data=data)
        post_soup = BeautifulSoup(response.content, 'html.parser')
        l = post_soup.find_all('span', id="wrongEmail")
        out.append({"name": name,"domain":domain,"method":method,"rate_limit":rate_limit,
                    "rateLimit": False,
                    "exists": l != [],
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
