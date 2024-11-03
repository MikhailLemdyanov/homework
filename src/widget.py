from masks import get_mask_card_number, get_mask_account

def mask_account_card(user_info: str) -> str:
    """Функция, маскирующая информацию как о картах, так и о счетах"""
    if 'Счет' in user_info:
        return ('Счет ' + get_mask_account(user_info))
    else:
        card_number = get_mask_card_number(user_info[-16:])
        card_mask = user_info.replace(user_info[-16:], card_number)
        return card_mask
