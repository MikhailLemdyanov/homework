import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture()
def cards() -> str:
    return "7000792289606361"


def test_get_mask_card_number(cards: str) -> None:
    assert get_mask_card_number(cards) == "7000 79** **** 6361"


@pytest.fixture()
def accounts() -> str:
    return "73654108430135874305"


def test_get_mask_account(accounts: str) -> None:
    assert get_mask_account(accounts) == "**4305"
