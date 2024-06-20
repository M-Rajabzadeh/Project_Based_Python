import random
import string
from nltk.corpus import words

# Download the words dataset (only needs to be done once)
import nltk
nltk.download('words')

def pin_password_generator(length: int) -> str:
    """
    Generates a random PIN password of a given length (only digits).

    Args:
    - length (int): Length of the PIN password.

    Returns:
    - str: Generated PIN password.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))

def random_password_generator(length=8, include_numbers=False, include_symbols=False) -> str:
    """
    Generates a random password of a given length with optional numbers and symbols.

    Args:
    - length (int): Length of the password.
    - include_numbers (bool): Whether to include numbers in the password.
    - include_symbols (bool): Whether to include symbols in the password.

    Returns:
    - str: Generated random password.
    """
    password_chars = string.ascii_letters
    if include_numbers:
        password_chars += string.digits
    if include_symbols:
        password_chars += string.punctuation
    return ''.join(random.choice(password_chars) for _ in range(length))

def memorize_password_generator(num_phrases=4, sep='_', uppercase=False) -> str:
    """
    Generates a memorable password using random words from NLTK's words corpus.
    Optionally converts some of the words to uppercase randomly.

    Args:
    - num_phrases (int): Number of words to be included in the password.
    - sep (str): Separator to be used between words.
    - uppercase (bool): Whether to randomly convert some words to uppercase.

    Returns:
    - str: Generated memorable password.
    """
    words_list = [random.choice(words.words()) for _ in range(num_phrases)]

    if uppercase:
        words_list = [word.upper() if random.choice([True, False]) else word for word in words_list]

    return sep.join(words_list)
