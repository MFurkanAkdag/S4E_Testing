import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.web]


def test_start_trial_and_see_plans_buttons_visible(home):
    # Start Trial butonu görünüyor mu?
    expect(home.start_trial_button).to_be_visible()

    # See the Plans butonu görünüyor mu?
    expect(home.see_plans_button).to_be_visible()
