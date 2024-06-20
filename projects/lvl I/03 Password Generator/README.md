# Password Generator

This project includes several functions for generating different types of passwords: PINs, random passwords with optional numbers and symbols, and memorable passwords using random words from NLTK's words corpus.

## Features

- **PIN Password Generator**: Generates a random PIN of a specified length (only digits).
- **Random Password Generator**: Generates a random password with options for including numbers and symbols.
- **Memorable Password Generator**: Generates a memorable password using random words, with options to randomly capitalize some words.

## Requirements

- Python 3.11+
- NLTK (Natural Language Toolkit)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/M-Rajabzadeh/Project_Based_Python
    cd project/lvl I/03 Password Generator/src/main.py
    ```

2. Install the required dependencies:
    ```sh
    pip install nltk
    ```

3. Download the NLTK words dataset (only needs to be done once):
    ```python
    import nltk==3.8.1
    nltk.download('words')
    ```

## Running the Project

Make sure you've installed all the required dependencies. You can then set your PYTHONPATH, navigate to the 'src' directory and run the project using Python:

```bash
export PYTHONPATH="${PYTHONPATH}:/your/path/to/main/directory"
cd src
python main.py
```

1. **PIN Password Generator**:
    ```python
    from src.main import pin_password_generator
    print(pin_password_generator(6))  # Generates a PIN with 6 digits
    ```

2. **Random Password Generator**:
    ```python
    from src.main import random_password_generator
    print(random_password_generator(length=8, include_numbers=True))  # Generates a random password with 8 characters including numbers
    print(random_password_generator(length=12, include_numbers=True, include_symbols=True))  # Generates a random password with 12 characters including numbers and symbols
    ```

3. **Memorable Password Generator**:
    ```python
    from src.main import memorize_password_generator
    print(memorize_password_generator(num_phrases=4, uppercase=True))  # Generates a memorable password with 4 words, some words in uppercase
    print(memorize_password_generator(num_phrases=6, sep='-'))  # Generates a memorable password with 6 words separated by '-'
    print(memorize_password_generator(num_phrases=5))  # Generates a memorable password with 5 words, random case
    ```

## Examples

```sh
    print("PIN Password (length 6):", pin_password_generator(6))
    print("Random Password (length 8, include numbers):", random_password_generator(length=8, include_numbers=True))
    print("Random Password (length 12, include numbers and symbols):", random_password_generator(length=12, include_numbers=True, include_symbols=True))
    print("Memorable Password (4 words, random case):", memorize_password_generator(num_phrases=4, uppercase=True))
    print("Memorable Password (6 words, separator '-'): ", memorize_password_generator(num_phrases=6, sep='-'))
    print("Memorable Password (5 words, mixed case):", memorize_password_generator(num_phrases=5))
```