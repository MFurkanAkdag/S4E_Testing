import pytest
from playwright.sync_api import expect

pytestmark = [pytest.mark.web]


def test_ctem_features_section_visible(home):
    expect(home.ctem_features_section).to_be_visible()

def test_ctem_features_card_visible(home):
    expect(home.ctem_feature_card).to_be_visible()