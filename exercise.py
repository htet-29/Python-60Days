password = input("Enter your password: ")


def password_strength(_password):
    result = {}

    length = len(_password)

    if length >= 8:
        result['length'] = True
    else:
        result['length'] = False


    upper = False
    digit = False

    for char in _password:
        if char.isupper():
            upper = True
        if char.isdigit():
            digit = True

    result['upper'] = upper
    result['digit'] = digit

    if all(result.values()):
        return "Strong password"
    else:
        return "Weak password"


print(password_strength(password))