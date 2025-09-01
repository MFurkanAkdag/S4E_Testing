import re
from playwright.sync_api import Page, expect
from src.config import Settings


class BasePage:
    def __init__(self, page: Page, settings: Settings):
        self.page = page
        self.settings = settings
        self.page.set_default_timeout(settings.TIMEOUT_MS)

    def goto(self, path: str = ""):
        base = self.settings.WEB_BASE_URL.rstrip("/")
        self.page.goto(f"{base}{path}", wait_until="domcontentloaded")

