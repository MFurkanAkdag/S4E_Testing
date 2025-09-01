from playwright.sync_api import Locator
from src.pages.base_page import BasePage


class ResourcesPage(BasePage):
    @property
    def blog_indicator(self) -> Locator:
        # /resources veya /blog gibi
        return self.page.locator("a[href*='/blog'], a[href*='/resources']").first

    def open(self):
        self.goto("/resources")
