import os
import re
from bs4 import BeautifulSoup
from collections import deque
from urllib.parse import unquote
from rich.console import Console

console = Console()

def read_file(name):
    with open(f"pages/{name}.html", "r", encoding="utf-8") as f:
        content = ""
        for l in f.readlines():
            content += l
    return content

def find_links(file):
    soup = BeautifulSoup(file, "html.parser")
    article = soup.find("div", {"id": "bodyContent"}) or soup.find("div", {"id": "mw-content-text"})
    if not article:
        return []

    links = article.find_all("a", href=re.compile("^/wiki/((?!:).)*$"))
    person_links = []

    for link in links:
        title = link["href"].split("/wiki/")[-1]
        title = unquote(title).replace("_", " ")

        file_path = f"pages/{title}.html"
        if os.path.exists(file_path):
            if title not in person_links:
                person_links.append(title)

    return person_links

def degrees_of_separation(start, target):
    if start == target:
        return 0, [start]

    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue
        visited.add(current)

        if not os.path.exists(f"pages/{current}.html"):
            continue
        file = read_file(current)
        neighbors = find_links(file)

        for neighbor in neighbors:
            if neighbor == target:
                return len(path), path + [neighbor]
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None, []

def main():
    name1 = input("Enter the first name: ")
    if not name1:
        console.print("[bold red]No name provided. Exiting.[/bold red]")
        return
    elif not os.path.exists(f"pages/{name1}.html"):
        console.print(f"[bold red]File 'pages/{name1}.html' does not exist. Exiting.[/bold red]")
        return
    
    name2 = input("Enter the second name: ")
    if not name2:
        console.print("[bold red]No name provided. Exiting.[/bold red]")
        return
    elif not os.path.exists(f"pages/{name2}.html"):
        console.print(f"[bold red]File 'pages/{name2}.html' does not exist. Exiting.[/bold red]")
        return
    
    file1 = read_file(name1)
    links1 = find_links(file1)

    print()
    console.print(f"[bold yellow]Links found in '{name1}.html':[/bold yellow]")
    for i, link in enumerate(links1, start=1):
        print(f"{i}. {link}")

    file2 = read_file(name2)
    links2 = find_links(file2)

    print()
    console.print(f"[bold yellow]Links found in '{name2}.html':[/bold yellow]")
    for i, link in enumerate(links2, start=1):
        print(f"{i}. {link}")

    print()
    sep, path = degrees_of_separation(name1, name2)
    if sep is not None:
        console.print(f"[bold green]{name1} to {name2} in {sep} steps:[/bold green]")
        console.print(" → ".join(path))
    else:
        console.print(f"[bold red]No connection found between {name1} and {name2}[/bold red]")

if __name__ == "__main__":
    main()