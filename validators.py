import random
import string


def check_email(email):
    if '@' not in email or '.' not in email:
        return False
    else:
        return True


def passwd_generator():
    symbols_pool = string.ascii_letters + string.digits
    return ''.join(random.sample(symbols_pool, 12))
