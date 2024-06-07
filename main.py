import random
import string


def generate_secure_password(length=12,
                             use_uppercase=True,
                             use_digits=True,
                             use_special=True,
                             exclude_ambiguous=False):
    """
    Generate a secure password with specified options.

    :param length: Length of the password (default is 12)
    :param use_uppercase: Include uppercase letters (default is True)
    :param use_digits: Include digits (default is True)
    :param use_special: Include special characters (default is True)
    :param exclude_ambiguous: Exclude ambiguous characters like 0, O, 1, l (default is False)
    :return: A secure password as a string
    """
    if length < 4:
        raise ValueError(
            "Password length should be at least 4 characters to include all character types."
        )

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_characters = string.punctuation if use_special else ''

    if exclude_ambiguous:
        ambiguous_chars = '0O1l'
        lowercase = ''.join([c for c in lowercase if c not in ambiguous_chars])
        uppercase = ''.join([c for c in uppercase if c not in ambiguous_chars])
        digits = ''.join([c for c in digits if c not in ambiguous_chars])
        special_characters = ''.join(
            [c for c in special_characters if c not in ambiguous_chars])

    all_characters = lowercase + uppercase + digits + special_characters

    if not all_characters:
        raise ValueError(
            "No characters available to generate password. Adjust your settings."
        )

    password = [
        random.choice(lowercase),
        random.choice(uppercase)
        if use_uppercase else random.choice(lowercase),
        random.choice(digits) if use_digits else random.choice(lowercase),
        random.choice(special_characters)
        if use_special else random.choice(lowercase)
    ]

    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)

    return ''.join(password)


def save_password_to_file(password, filename="passwords.txt"):
    """
    Save the generated password to a file.

    :param password: The password to save
    :param filename: The filename to save the password to (default is "passwords.txt")
    """
    with open(filename, 'a') as file:
        file.write(password + '\n')
    print(f"Password saved to {filename}")


if __name__ == "__main__":
    try:
        length = int(
            input("Enter the desired length of the password (minimum 4): "))
        if length < 4:
            raise ValueError(
                "Password length should be at least 4 characters.")

        use_uppercase = input(
            "Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_digits = input(
            "Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special = input(
            "Include special characters? (yes/no): ").strip().lower() == 'yes'
        exclude_ambiguous = input(
            "Exclude ambiguous characters (0, O, 1, l)? (yes/no): ").strip(
            ).lower() == 'yes'

        password = generate_secure_password(length, use_uppercase, use_digits,
                                            use_special, exclude_ambiguous)
        print(f"Generated secure password: {password}")

        save = input("Do you want to save the password to a file? (yes/no): "
                     ).strip().lower()
        if save == 'yes':
            save_password_to_file(password)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
