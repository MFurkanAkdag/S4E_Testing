import re
from playwright.sync_api import Locator
from src.pages.base_page import BasePage

class HomePage(BasePage):
    @property
    def join_link(self) -> Locator:
        # "Join" butonunu metinden yakala (link veya button olabilir)
        return self.page.get_by_role("link", name="Join").or_(
            self.page.get_by_role("button", name="Join")
        )

    @property
    def ctem_features_section(self) -> Locator:
        return self.page.get_by_role("heading", name=re.compile(r"CTEM\s*Features", re.I))

    @property
    def ctem_feature_card(self) -> Locator:
        # Birden fazla aynı başlık varsa ilkini seç
        return self.page.locator("h4", has_text=re.compile(r"Effortless\s+Security\s+Automation", re.I)).first

    @property
    def resources_section(self) -> Locator:
        return self.page.get_by_role("heading", name=re.compile(r"Check Out More Resources", re.I))

    @property
    def resources_link(self) -> Locator:
        return self.page.locator("p:has-text('Check Out More Resources')")

    @property
    def start_trial_button(self) -> Locator:
        return self.page.get_by_role("link", name=re.compile(r"start\s*trial", re.I))

    @property
    def see_plans_button(self) -> Locator:
        return self.page.get_by_role("link", name=re.compile(r"see\s*the\s*plans", re.I))

    def open(self):
        self.goto("/")