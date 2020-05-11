def handle_error_1(get_account_balance):
    def wrapper(*args):
        try:
            return get_account_balance(*args)
        except TypeError:
            print('No username defined!')
    return wrapper

def handle_error_2(change_password):
    def wrapper(*args):
        try:
            return change_password(*args)
        except TypeError:
            print('No password to change!')
    return wrapper


@handle_error_1('get_account_balance')
@handle_error_2('change_password')
class User:
    def __init__(self):
        pass

    def get_account_balance(self):
        pass

    def change_password(self):
        pass
    
u = User()
u.get_account_balance()
u.change_password()
