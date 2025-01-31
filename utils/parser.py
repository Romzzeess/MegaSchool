import requests

from bs4 import BeautifulSoup
from googlesearch import search


async def async_get_context(question: str, num_sources: int=2) -> tuple[list[str], list[str]]:
    """Functions to parse information from itmo websites with google"""
    
    # search in google
    links = []
    search_results = search(question, tld="co.in", num=num_sources, stop=num_sources, pause=0.2)
    for search_result in search_results:
        links.append(search_result)
    
    texts = []
    right_links = []
    
    # parse itmo links
    for link in links:
         if "itmo" in link:
            response = requests.get(link)
            soup = BeautifulSoup(response.text, "html.parser")
            texts.append(str(soup.find_all("p")))
            right_links.append(link)
            
    return " ".join(texts), right_links
