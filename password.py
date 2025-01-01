PASSWORD = input("Введите пароль: ")


def main():
    def is_very_long(PASSWORD):
        return len(PASSWORD) > 12

         
    def has_digit(PASSWORD):
        return any(i.isdigit() for i in PASSWORD)


    def has_upper_letters(PASSWORD):
        return any(i.isupper() for i in PASSWORD)


    def has_lower_letters(PASSWORD):
        return any(i.islower() for i in PASSWORD)


    def has_symbols(PASSWORD):
        return any(i in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for i in PASSWORD)
    

    list_function = [
        is_very_long,
        has_digit,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]

    score = 0


    for function in list_function:
        if function(PASSWORD):
            score += 2


    print(f"Рейтинг пароля: {score}")


if __name__ == "__main__":
    main()
