import random
import string


def password_generator(char_num:int,includes:list=[1,2,3,4],check_strength:bool=False):
    #includes ro tabdil be ye list az char haye entekhabi kardam , masalan:all_chars=[["a","b",..],["A","B",..],..]
    all_chars=[]

    #is it necessary?
    if char_num == 0:
        if check_strength:
            return ['', None]
        else:
            return ''


    if 1 in includes:
        all_chars.extend(list(string.ascii_lowercase))
    if 2 in includes:
        all_chars.extend(list(string.ascii_uppercase))
    if 3 in includes:
        all_chars.extend(list(string.digits))
    if 4 in includes:
        all_chars.extend(["@","%","!","#","$","^","&","*"])
    

    random.shuffle(all_chars)
    password="".join(all_chars[5:char_num+5])

    import password_checker
    
    if check_strength:
        return[password,password_checker.check_password_strength(password)]
    else:
        return password
    
    
print(password_generator(10,check_strength=False))