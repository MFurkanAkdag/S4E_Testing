from playwright.sync_api import Locator, expect
from src.pages.base_page import BasePage


class PricingPage(BasePage):
    @property
    def yearly_toggle(self) -> Locator:
        # "Pay yearly" textini içeren element
        return self.page.locator("h6:has-text('Pay yearly')")

    @property
    def monthly_toggle(self) -> Locator:
        # "Pay monthly" textini içeren element
        return self.page.locator("h6:has-text('Pay monthly')")

    def open(self):
        self.goto("/pricing")

    def assert_toggle_accessible(self):
        expect(self.yearly_toggle).to_be_visible()
        expect(self.monthly_toggle).to_be_visible()

    @property
    def plan_wizard_button(self) -> Locator:
        # Direkt text üzerinden butonu yakala
        return self.page.get_by_role("button", name="Plan wizard")

    @property
    def plan_wizard_popup(self) -> Locator:
        # Popup genelde dialog/modal olur
        return self.page.locator("[role='dialog'], .modal, .ant-modal").first