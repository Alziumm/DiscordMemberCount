import requests, re
from bs4 import BeautifulSoup

def extract_numbers(text : str) -> str or None:

    match = re.search(r'\b\d{1,3}(,\d{3})*\b', text)

    if len(match) == 0 or match is None:

        return None
    
    return match.group(0)

def get_member_count(invite_link : str) -> str:

    if "https://discord.com/" not in invite_link and "https://discord.gg/" not in invite_link:

        return "NULL"

    try:
        response = requests.get(invite_link)
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