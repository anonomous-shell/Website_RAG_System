from urllib.parse import urljoin, urlparse
from collections import deque
import requests
from bs4 import BeautifulSoup


def crawl_website(start_url, max_pages=30):
    """
    Crawl all internal links of a website.

    Returns:
        list[str] -> URLs
    """

    visited = set()

    queue = deque([start_url])

    urls = []

    domain = urlparse(start_url).netloc

    while queue and len(urls) < max_pages:

        url = queue.popleft()

        if url in visited:
            continue

        visited.add(url)

        try:

            response = requests.get(
                url,
                timeout=10,
                headers={
                    "User-Agent":
                    "Mozilla/5.0"
                }
            )

            if response.status_code != 200:
                continue

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            urls.append(url)

            for tag in soup.find_all("a", href=True):

                link = urljoin(
                    url,
                    tag["href"]
                )

                parsed = urlparse(link)

                if parsed.netloc != domain:
                    continue

                clean_url = parsed.scheme + "://" + parsed.netloc + parsed.path

                if clean_url not in visited:
                    queue.append(clean_url)

        except Exception:

            pass

    return urls