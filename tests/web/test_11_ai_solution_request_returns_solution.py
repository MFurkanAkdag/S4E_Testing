import pytest
from playwright.sync_api import expect
from src.pages.ai_solution_page import AiSolutionPage

pytestmark = [pytest.mark.web]


def test_ai_solution_request(page, settings):
    ai_page = AiSolutionPage(page, settings)
    ai_page.open()

    # Butona tıkla
    ai_page.get_solution_button.click()

    # Çıktı başlığı görünüyor mu?
    expect(ai_page.solution_output).to_be_visible(timeout=10000)
