from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime
import httpx
from bs4 import BeautifulSoup


class BaseScraper(ABC):
    source: str = ""
    source_type: str = ""  # banco, fintech, prepaga
    base_url: str = ""

    def __init__(self):
        self.session = httpx.Client(
            headers={"User-Agent": "Mozilla/5.0 (compatible; MeDescuentosBot/1.0)"},
            timeout=30,
            follow_redirects=True,
        )

    @abstractmethod
    def scrape(self) -> List[Dict]:
        """Extrae los descuentos y retorna una lista de dicts con los datos."""
        pass

    def fetch(self, url: str) -> BeautifulSoup:
        response = self.session.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, "lxml")

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
