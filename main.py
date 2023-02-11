import requests, re
from bs4 import BeautifulSoup

def extract_numbers(text : str) -> str or None:

    match = re.search(r'\b\d{1,3}(,\d{3})*\b', text)

    if len(match.group(0)) == 0 or match.group(0) is None:

        return None
    
    return match.group(0)

def get_member_count(invite_link : str) -> str:

    if "https://discord.com/" not in invite_link and "https://discord.gg/" not in invite_link:

        return "NULL"

    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36","Accept": "application/json","Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3","Accept-Encoding": "gzip, deflate","Connection": "keep-alive"}
        response = requests.get(invite_link, headers=headers)
    except:
        return "NULL"

    if response.status_code != 200:
        
        return "NULL"
    
    try:
        soup = BeautifulSoup(response.text, "html.parser")
        member_count_tag = soup.find("meta", property="og:description")
        data = extract_numbers(str(member_count_tag))
    except:
        return "NULL"

    if data is None or data == "" or len(data) == 0:

        return "NULL"

    return data

member_count = get_member_count("https://discord.gg/exemple")

print(member_count)