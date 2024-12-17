import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../Bank_App/logs/masks.log", 'w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def get_mask_card_number(card_number: str) -> str:
    """Функция, маскирующая номер карты"""
    logger.info("Выполняется проверка правильности номера карты")
    card_number_str = str(card_number)
    if len(card_number_str) != 16 or not card_number_str.isdigit():
        logger.error('Неверный номер карты!')
        raise ValueError('Неверный номер карты.')
    card_number_mask = f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    logger.info("Номер карты замаскирован")
    return card_number_mask


def get_mask_account(account_number: str) -> str:
    """Функция, маскирующая номер счета"""
    logger.info("Выполняется проверка правильности номера карты")
    account_number_str = str(account_number)
    if len(account_number_str) != 20 or not account_number_str.isdigit():
        logger.error('Неверный номер счета!')
        raise ValueError('Неверный номер счета.')
    account_number_mask = f"**{account_number_str[-4:]}"
    logger.info("Номер счета замаскирован")
    return account_number_mask
