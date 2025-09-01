import re
import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.web, pytest.mark.smoke]


def test_join_button_navigates_to_signup(home):
    home.join_link.click()
    expect(home.page).to_have_url(re.compile(r"app\.s4e\.io/sign-?up", re.I))
