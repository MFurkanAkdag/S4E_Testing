import re
from playwright.sync_api import Locator
from src.pages.base_page import BasePage


class AiSolutionPage(BasePage):
    def open(self):
        self.goto("/features/ai-based-solutions")

    @property
    def get_solution_button(self) -> Locator:
        return self.page.get_by_role("button", name=re.compile(r"Get AI Solution", re.I))

    @property
    def solution_output(self) -> Locator:
        return self.page.get_by_role("heading", name=re.compile(r"AI\s*-\s*Based\s*Solution\s*Advices", re.I))
