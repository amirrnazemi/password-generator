import string

from random import shuffle, choice
from typing import Union


def check_password_strength(password: str, tagged: bool = True)->Union[str, int]:

    password_point = 0
    tags = {90: 'very strong', 75: 'strong', 50: 'medium', 25: 'weak', 0: 'very weak'}
    
    password_point = len(password) * 5
    
    password_point = max(min(password_point, 100), 0)
    
    if tagged:
        for min, tag in tags:
            if password_point >= min:
                return tag
        return tags[0]
    else:
        return password_point