def username_len(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def username_isalnum(name):
    for characters in name:
        if not (characters.isalnum() or characters == "-" or characters == "_"):
            return False
        return True


def no_redundant_symbols(name):
    if " " in name:
        return False
    return True


def valid_username(name):
    if username_len(name) and username_isalnum(name) and no_redundant_symbols(name):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if valid_username(username):
        print(username)

