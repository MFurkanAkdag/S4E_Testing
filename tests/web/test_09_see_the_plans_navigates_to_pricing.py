import re
import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.web]


def test_see_plans_redirects_to_pricing(home):
    home.see_plans_button.click()
    expect(home.page).to_have_url(re.compile(r"s4e\.io/pricing", re.I))
