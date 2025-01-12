from masks import get_mask_account, get_mask_card_number


def mask_account_card(user_info: str) -> str:
    """Функция, маскирующая информацию как о картах, так и о счетах"""
    info_list = user_info.split(" ")
    if info_list[0] == "Счет":

        return f"Счет {get_mask_account(info_list[1])}"

    else:

        joined_info = " ".join(info_list[:-1])
        return f"{joined_info} {get_mask_card_number(info_list[-1])}"


def get_date(date: str) -> str:
    """Функция, которая возвращает дату в формате ДД.ММ.ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
