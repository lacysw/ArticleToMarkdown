import sys, requests, datetime
from bs4 import BeautifulSoup as bs

# reuters.com
def reuters(soup):
    # Title
    result = "# Reuters: " + soup.find("div", {"class": "article-header__heading__15OpQ"}).find("h1").get_text() + "\n\n"

    # Body
    body = soup.find("div", {"class": "paywall-article"}).find_all("p")
    for p in body:
        result += "> " + p.get_text() + "\n>\n"
    
    return result

def main():
    # Chrome 99 on Windows 10
    user_agent = "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"
    response = requests.get(sys.argv[1], headers = {"user_agent": user_agent})

    if(response.status_code != 200):
        print("Error: received code " + response.status_code)
        exit()

    soup = bs(response.content, features="lxml")
    now = datetime.datetime.utcnow().strftime("%Y/%m/%d at %H:%M:%S")

    result = reuters(soup) + f"\n\n---\n\n*Retrieved from [{sys.argv[1]}](sys.argv[1]) on {now} UTC*"

    print(result)

if __name__ == "__main__":
    main()
