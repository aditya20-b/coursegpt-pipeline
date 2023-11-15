from bs4 import BeautifulSoup
import asyncio
import aiohttp

class InfoScraper:
    def __init__(self):
        self.info = {}

    
    def __repr__(self):
        return f"InfoScraper(info={self.info})"
    
    async def get_info(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")
                title = soup.find("title").text
                self.info[url] = title
                return self.info