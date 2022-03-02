def func(x):
    return x + 1

# More elaborated version (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Tell me your email: ")

    #if ("@" not in email or "." not in email):
    if ("@" not in email or "." not in email):
        print('Email is not valid.')
        return None
    else:
        return email

#get_email_from_input()
