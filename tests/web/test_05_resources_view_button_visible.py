import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.web]


def test_resources_link_visible(home):
    # "Check Out More Resources" başlığı görünsün
    home.resources_section.scroll_into_view_if_needed()

    expect(home.resources_section).to_be_visible()

    expect(home.resources_link).to_be_visible()
