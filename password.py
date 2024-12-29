password = input("Введите пароль: ")
len_str = len(password)
score = 0


def is_very_long(password):
    if len_str > 12:
        return True
    else:
        return False


def has_digit(password):
    for i in password:
        if i.isdigit():
            return True
    return False


def has_upper_letters(password):
    for i in password:
        if i.isupper():
            return True
    return False


def has_lower_letters(password):
    for i in password:
        if i.islower():
            return True
    return False


symbols = "!@#$%^&*()-_=+[]{}|;:'"


def has_symbols(password):
    for i in password:
        if i in symbols:
            return True
    return False


list_function = [
    is_very_long,
    has_digit,
    has_upper_letters,
    has_lower_letters,
    has_symbols
]


for function in list_function:
    if function(password):
        score += 2


print(f"Рейтинг пароля: {score}")
