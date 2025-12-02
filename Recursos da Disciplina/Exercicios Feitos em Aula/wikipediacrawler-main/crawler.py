import re
import os
import requests
import time
from bs4 import BeautifulSoup
from rich.console import Console

console = Console()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
url_base = "https://pt.wikipedia.org"
homepage = "/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal"

def is_person_page(soup):
    box = soup.find("table", {"class": re.compile("infobox")})
    if not box:
        return False
    tags = [tag.get_text(strip=True) for tag in box.find_all("th")]
    return any("Nascimento" in tag for tag in tags)

def get_person_name(soup):
    title_tag = soup.find("span", {"class": "mw-page-title-main"})
    if title_tag:
        return title_tag.get_text(strip=True)
    return None

def save_person_page(name, content):
    os.makedirs("pages", exist_ok=True)
    with open(f"pages/{name}.html", "w", encoding="utf-8") as f:
        f.write(content)

def get_page_links(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        article = soup.find("div", {"id": "bodyContent"}) or soup.find("div", {"id": "mw-content-text"})
        if not article:
            return []
        all_links = article.find_all("a", href=re.compile("^/wiki/((?!:).)*$"))
        return [url_base + link["href"] for link in all_links if link.get("href")]
    except:
        return []

def crawl(url, people, visited, limit=1000):
    if len(people) >= limit:
        return

    if url in visited:
        return
    visited.add(url)

    console.print(f"[bold yellow]Reading page: {url}[/bold yellow]")

    links = get_page_links(url)
    found_new_person = False

    for link in links:
        if len(people) >= limit:
            return
        if link in visited:
            continue

        try:
            response = requests.get(link, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, "html.parser")
            print(f"Visiting link: {link}")
        except:
            continue

        if is_person_page(soup):
            name = get_person_name(soup)
            if name and name not in people:
                people.add(name)
                # save_person_page(name, response.content.decode("utf-8"))
                # console.print(f"[bold green]'{name}.html' was saved[/bold green]")
                console.print(f"[bold green]Person found: {name}[/bold green]")
                time.sleep(1)

                found_new_person = True
                crawl(link, people, visited, limit)

    if not found_new_person and len(people) < limit:
        homepage_url = url_base + homepage
        console.print("[bold red]Dead end reached. Restarting from homepage...[/bold red]")
        crawl(homepage_url, people, visited, limit)

def main():
    start_time = time.time()

    people = set()
    visited = set()
    homepage_url = url_base + homepage
    crawl(homepage_url, people, visited, limit=1000)

    end_time = time.time()

    console.print(f"\nPeople collected: {len(people)}", style="bold blue")
    console.print(f"Time taken: {end_time - start_time:.2f} seconds", style="bold blue")

if __name__ == "__main__":
    main()