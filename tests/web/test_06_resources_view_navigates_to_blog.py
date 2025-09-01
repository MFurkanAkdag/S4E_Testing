import re
import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.web]


def test_resources_link_redirects_to_blog(home):
    home.resources_section.scroll_into_view_if_needed()
    home.resources_link.click()
    expect(home.page).to_have_url(re.compile(r"resources\.s4e\.io/blog", re.I))
