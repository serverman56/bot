# make a function to get all repo links of a user in github
import requests
from bs4 import BeautifulSoup


def get_all_repo_links(username):
    """Get all repo links of a user in github"""
    url = f"https://github.com/{username}?tab=repositories"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    repo_links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href.startswith(f"/{username}/"):
            repo_links.append(f"https://github.com{href}")
    return repo_links


repoLinks = get_all_repo_links("OCEANOFANYTHINGOFFICIAL")
for link in repoLinks:
    print(link)
