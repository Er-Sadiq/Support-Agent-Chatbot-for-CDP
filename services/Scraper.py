import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.parse import urlparse, urljoin

def doc_Scaper(url, platform):
    try:
        res = requests.get(url)
        res.raise_for_status()  
        soup = BeautifulSoup(res.content, 'html.parser')
        
        content = []
        for i in soup.find_all(['h1', 'h2', 'h3', 'p']):
            text = i.get_text(strip=True)
            if text:
                content.append({'platform': platform, 'content': text})
        
        return content
    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return []

def get_internal_links(base_url):
    try:
        res = requests.get(base_url)
        res.raise_for_status()
        soup = BeautifulSoup(res.content, 'html.parser')
        
        internal_links = set()
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Resolve relative URLs to absolute ones
            full_url = urljoin(base_url, href)
            
            # Check if the link is within the same domain
            if urlparse(full_url).netloc == urlparse(base_url).netloc:
                internal_links.add(full_url)
        
        return internal_links
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving internal links from {base_url}: {e}")
        return set()


urls = {
    "Segment": "https://segment.com/docs/",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

data = []


for platform, url in urls.items():
    print(f"Scraping {platform} main URL: {url}")
    # Scrape the main page
    data.extend(doc_Scaper(url, platform))
    
    # Get all internal links on the main page
    internal_links = get_internal_links(url)
    
    # Scrape each internal link
    for link in internal_links:
        print(f"Scraping internal link: {link}")
        data.extend(doc_Scaper(link, platform))

# Create a 'data' folder if it doesn't exist
os.makedirs('data', exist_ok=True)

# Save the scraped data to JSON
with open('data/cdp_docs.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Documentation scraped and saved.")


if __name__ == "__main__":
    doc_Scaper()
