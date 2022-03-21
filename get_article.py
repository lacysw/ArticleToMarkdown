#!/usr/bin/env python3

import requests # Webpage grabbing
import tldextract # Determine site from URL
from markdownify import markdownify as md # Markdown formatting
from datetime import datetime as dt # Timestamp on result footer
from bs4 import BeautifulSoup as bs # HTML parsing

# reuters.com
def reuters(soup):
    # Title
    # `article-header__heading__15OpQ` is the div which contains the article title
    result = "# Reuters: " + soup.find("div", {"class": "article-header__heading__15OpQ"}).find("h1").get_text() + "\n"

    # Body
    # `paywall-article` is the div which contains the article text
    body = soup.find("div", {"class": "paywall-article"}).find_all("p")
    for p in body:
        p = str(p)
        p = p.replace(' href="/', ' href="https://reuters.com/') # Make relative links absolute
        p = md(p) # Strip usless HTML tags; format links
        p = "\n> " + p.strip() + "\n>" # Format as blockquote
        result += p

    result = "\n".join(result.split("\n")[0:-1]) # Remove trailing '>'
    return result

def main(url):
    # Chrome 99 on Windows 10
    user_agent = "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"
    response = requests.get(url, headers = {"user_agent": user_agent})

    if(response.status_code != 200):
        print(f"Error: received code {response.status_code} from {url}")
        return 1

    soup = bs(response.content, features="lxml")
    domain = tldextract.extract(url)[1]
    now = dt.utcnow().strftime("%Y/%m/%d at %H:%M:%S")
    footer = f"\n\n---\n\n*Retrieved from [{url}]({url}) on {now} UTC*."

    if(domain == "reuters"):
        result = reuters(soup) + footer
    else:
        result = f"[!] Error: {domain} is not yet supported."

    return result

if __name__ == "__main__":
    main()
