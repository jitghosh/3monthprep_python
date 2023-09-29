def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    numbers_count = 0
    lowercase_count = 0
    uppercase_count = 0
    special_characters_count = 0

    # count how many of each type we have
    for c in password:
        if c in numbers:
            numbers_count += 1
        elif c in lower_case:
            lowercase_count += 1
        elif c in upper_case:
            uppercase_count += 1
        elif c in special_characters:
            special_characters_count += 1

    # count how many we fall short by 
    char_category_shortfall = (max(0,(1 - numbers_count)) + 
                    max(0,(1 - lowercase_count)) + 
                    max(0,(1 - uppercase_count)) + 
                    max(0,(1 - special_characters_count)))
    # Ex 1. say we have a password of length 4 (all uppercase). Then we 
    # fall short by 3 (since we need at least one number, one lowercase 
    # and one special char). So we will need max(3, 6 - 4) i.e.3 more to cover 
    # both the category requirements as well as the total length (6) requirement 
    # Ex 2. Say we have a password of length 2 (All numbers). 
    # Again we have a shortfall of 3 (uppercase, lowercase and special char). But 
    # adding 3 is not enough as that will make it 5 but we need a total length of 6.
    # So max (3, 6 - 2) = 4 is what we need to add.
    chars_needed = max(char_category_shortfall,6 - len(password))

    return chars_needed
