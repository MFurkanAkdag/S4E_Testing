import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.web]


def test_plan_wizard_opens(pricing):
    pricing.plan_wizard_button.click()
    expect(pricing.plan_wizard_popup).to_be_visible()
