import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Cinema_of_India"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    if soup.title:
        print("Page Title:", soup.title.text)
    else:
        print("Title tag nahi mila!")

    links = soup.find_all("a")

    print(f"Total {len(links)} links mile.")
else:
    print(f"Error! Status Code: {response.status_code}")
