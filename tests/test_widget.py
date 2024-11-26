import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture()
def card() -> str:
    return "Visa Platinum 7000792289606361"


@pytest.fixture()
def account() -> str:
    return "Счет 73654108430135874305"


def test_mask_account_card_by_card(card: str) -> None:
    assert mask_account_card(card) == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_by_account(account: str) -> None:
    assert mask_account_card(account) == "Счет **4305"


@pytest.fixture()
def dates() -> str:
    return "2024-03-11T02:26:18.671407"


def test_get_date(dates: str) -> None:
    assert get_date(dates) == "11.03.2024"
