def is_very_long(password):
    return len(password) > 12

         
def has_digit(password):
    return any(i.isdigit() for i in password)


def has_upper_letters(password):
    return any(i.isupper() for i in password)


def has_lower_letters(password):
    return any(i.islower() for i in password)


def has_symbols(password):
    return any(not i.isdigit() and i.isalpha() for i in password)

    
def main():
    password = input("Введите пароль: ")

    list_function = [
        is_very_long,
        has_digit,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]

    score = 0


    for function in list_function:
        if function(password):
            score += 2


    print(f"Рейтинг пароля: {score}")


if __name__ == "__main__":
    main()

