from playwright.sync_api import Locator
from src.pages.base_page import BasePage


class Footer(BasePage):
    @property
    def linkedin_button(self) -> Locator:
        return self.page.locator("a[href*='linkedin.com']").first

    @property
    def x_button(self) -> Locator:
        # Hem twitter.com hem x.com ihtimallerini kapsa
        return self.page.locator("a[href*='twitter.com'], a[href*='x.com']").first
