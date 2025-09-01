import pytest
from playwright.sync_api import Page
from src.config import Settings
from src.pages.home_page import HomePage
from src.pages.pricing_page import PricingPage


@pytest.fixture(scope="session")
def settings() -> Settings:
    return Settings.load()

@pytest.fixture()
def home(page: Page, settings: Settings) -> HomePage:
    h = HomePage(page, settings)
    h.open()
    return h

@pytest.fixture()
def pricing(page: Page, settings: Settings) -> PricingPage:
    p = PricingPage(page, settings)
    p.open()
    return p

