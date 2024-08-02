import random
import string
import password_checker

def password_generator(char_num:int,includes:list=[1,2,3,4],check_strength:bool=False):
    
    all_chars=[]

    if char_num == 0:
        if check_strength:
            return ['', None]
        else:
            return ''

    if type(includes)!=list or not len(includes):
        includes=[1,2,3,4]

    if 1 in includes:
        all_chars.extend(list(string.ascii_lowercase))
    if 2 in includes:
        all_chars.extend(list(string.ascii_uppercase))
    if 3 in includes:
        all_chars.extend(list(string.digits))
    if 4 in includes:
        all_chars.extend(["@","%","!","#","$","^","&","*"])
    

    random.shuffle(all_chars)

    password_list=[]
    for i in range(char_num):
        password_list.append(random.choice(all_chars))
    password="".join(password_list)


    
    if check_strength:
        return[password,password_checker.check_password_strength(password)]
    else:
        return password