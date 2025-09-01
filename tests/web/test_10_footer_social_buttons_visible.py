import pytest
from playwright.sync_api import expect
from src.pages.footer import Footer

pytestmark = [pytest.mark.web]


def test_footer_social_buttons_visible(home):
    footer = Footer(home.page, home.settings)

    # Footer'a kaydır
    footer.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # LinkedIn butonu görünüyor mu?
    expect(footer.linkedin_button).to_be_visible()

    # Twitter (X) butonu görünüyor mu?
    expect(footer.x_button).to_be_visible()
