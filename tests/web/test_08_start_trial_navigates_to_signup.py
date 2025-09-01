import re
import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.web]


def test_start_trial_redirects_to_signup(home):
    home.start_trial_button.click()
    expect(home.page).to_have_url(re.compile(r"app\.s4e\.io/sign-up", re.I))
