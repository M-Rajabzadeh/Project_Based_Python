import streamlit as st
from password_generators import pin_password_generator, random_password_generator, memorize_password_generator
from nltk.corpus import words

# Display a banner image at the top of the app
st.image('./images/banner.jpeg', width=700)

# Create a radio button for selecting the type of password generator
option = st.radio(
    'Choose a password generator',
    ('PIN Password', 'Random Password', 'Memorable Password'),
    captions=["PIN (4-32)", "Random (8-32)", "Memorable (words)"]
)

# Handle the option selected by the user
if option == 'PIN Password':
    # Create a slider for selecting the length of the PIN password
    length = st.slider("Select your number", 4, 32, 8)
    # Display the generated PIN password
    st.write(f'Your password is `{pin_password_generator(length)}`')

elif option == 'Random Password':
    # Create a slider for selecting the length of the random password
    length = st.slider("Select your number", 8, 32, 8)
    # Toggle options for including numbers and symbols in the random password
    include_numbers = st.toggle("Include numbers")
    include_symbols = st.toggle("Include symbols")
    # Display the generated random password
    st.write(
        f'Your password is ``` {random_password_generator(length=length, include_numbers=include_numbers, include_symbols=include_symbols)} ```'
    )

elif option == 'Memorable Password':
    # Create a slider for selecting the number of phrases in the memorable password
    num_phrases = st.slider("Select your number", 4, 12, 4)
    # Input box for the separator between phrases
    sep = st.text_input("Write your separator", "_")
    # Toggle option for converting the password to uppercase
    uppercase = st.toggle("Convert to uppercase")
    # Display the generated memorable password
    st.write(f'Your password is `{memorize_password_generator(num_phrases=num_phrases, sep=sep, uppercase=uppercase)}`')
