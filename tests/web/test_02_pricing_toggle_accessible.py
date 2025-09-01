import pytest

pytestmark = [pytest.mark.web]


def test_pricing_yearly_monthly_switch_is_accessible(pricing):
    pricing.assert_toggle_accessible()
