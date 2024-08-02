import string

from random import shuffle, choice
from typing import Union
from password_checker import check_password_strength


def password_generator(char_num: int, includes: list = [], check_strength: bool = False)->Union[str, list]:
    """_summary_

    Args:
        char_num (int): _description_
        includes (list, optional): _description_. Defaults to [].
        check_strength (bool, optional): _description_. Defaults to False.

    Returns:
        Union[str, list]: _description_
    """    
    password = []
    chars = []
    
    if char_num == 0:
        if check_strength:
            return ['', None]
        else:
            return ''
                
    if type(includes) != list or not len(includes):
        includes = [1, 2, 3, 4]

    # "1:lowercase let, 2:uppercase let, 3:numbers, 4:special signs"
    
    if 1 in includes:
        # لیست حروف کوچک انگلیسی به صورت به‌ هم‌ ریخته
        lowercase_letters = list(string.ascii_lowercase)
        shuffle(lowercase_letters)
        chars.extend(lowercase_letters)
        
    if 2 in includes:
        # لیست حروف بزرگ انگلیسی به صورت به‌ هم‌ ریخته
        uppercase_letters = list(string.ascii_uppercase)
        shuffle(uppercase_letters)
        chars.extend(uppercase_letters)

    if 3 in includes:
        # لیست اعداد به صورت به‌ هم‌ ریخته
        digits = list(string.digits)
        shuffle(digits)
        chars.extend(digits)

    if 4 in includes:
        # لیست کاراکترهای خاص به صورت به‌ هم‌ ریخته
        # special_characters = list(string.punctuation)
        special_characters = ["@","%","!","#","$","^","&","*"]
        shuffle(special_characters)
        chars.extend(special_characters)
        
    for _ in range(char_num + 5):
        password.append(choice(chars))
        
    password = ''.join(password[3:char_num + 3])
    
    if check_strength:
        return [password, check_password_strength(password=password)]
    else:
        return password