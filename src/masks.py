def get_mask_card_number(card_number: str) -> str:
    """Функция, маскирующая номер карты"""
    card_number_str = str(card_number)
    card_number_mask = f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    return card_number_mask


def get_mask_account(account_number: str) -> str:
    """Функция, маскирующая номер счета"""
    account_number_str = str(account_number)
    account_number_mask = f"**{account_number_str[-4:]}"
    return account_number_mask
