import requests
import re

from bs4 import BeautifulSoup
from googlesearch import search


CLEANR = re.compile('<.*?>')

def clean_str_html(raw_html: str) -> str:
    """Function to clean parsed text from html tags"""
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext

async def async_get_context(question: str, num_sources: int=2) -> tuple[str, list[str]]:
    """Functions to parse information from websites searched in google"""
    
    # search in google
    links = []
    search_results = search(question, tld="co.in", num=num_sources, stop=num_sources, pause=0.2)
    for search_result in search_results:
        links.append(search_result)
    
    texts = []
    
    # parse links
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")
        texts.append(clean_str_html(str(soup.find_all("p"))))
            
    return " . ".join(texts), links
