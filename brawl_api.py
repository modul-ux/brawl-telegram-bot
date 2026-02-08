import aiohttp

API_URL = "https://api.brawlstars.com/v1"
HEADERS = {}

def set_token(token):
    global HEADERS
    HEADERS = {"Authorization": f"Bearer {token}"}

async def get_club(tag):
    tag = tag.replace("#", "%23")
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.get(f"{API_URL}/clubs/{tag}") as r:
            return await r.json()
