from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_info: str) -> str:
    """Функция, маскирующая информацию как о картах, так и о счетах"""
    if "Счет" in user_info:
        return f"Счет {get_mask_account(user_info)}"
    else:
        card_number = get_mask_card_number(user_info[-16:])
        card_mask = user_info.replace(user_info[-16:], card_number)
        return card_mask


def get_date(date: str) -> str:
    """Функция, которая возвращает дату в формате ДД.ММ.ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
