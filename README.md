# **Holehe-X - Email to Account Details**
![PyPI - License](https://img.shields.io/pypi/l/holehe)

## **Summary**
*Efficiently finding registered accounts from emails.*

Holehe checks if an email is attached to an account on sites like twitter, instagram, imgur and more than 120 others.
+ Retrieves information using the forgotten password function.

## 🛠️ Installation
### With Github

```bash
git clone https://github.com/CyberDefenseEd/holehe-x
cd holehe-x/
python3 setup.py install
```

## Module Output
For each module, data is returned in a standard dictionary with the following json-equivalent format :
```json
{
  "name": "example",
  "rateLimit": false,
  "exists": true,
  "emailrecovery": "ex****e@gmail.com",
  "phoneNumber": "0*******78",
  "others": null
}
```

- rateLitmit : Lets you know if you've been rate-limited.
- exists : If an account exists for the email on that service.
- emailrecovery : Sometimes partially obfuscated recovery emails are returned.
- phoneNumber : Sometimes partially obfuscated recovery phone numbers are returned.
- others : Any extra info.
