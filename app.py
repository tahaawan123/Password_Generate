import streamlit as st
import random
import string

def generate_password(length,use_digits,use_special):
    characters = string.ascii_letters

    if use_digits:
        characters +=string.digits

    if use_special:
        characters +=string.punctuation

    return ''.join(random.choice(characters)for _ in range(length))



st.title(" 🔐 Password Generator")
st.markdown(
    """
       <style>
           div.stButton > button {
           color: #fff;
           background-color: #000;
           }

          

    </style>
    """,
    unsafe_allow_html=True
)



length = st.slider("Select Password Length", min_value=8, max_value=25, value=12)

use_digits = st.checkbox("Use Digits")

use_special = st.checkbox("Use Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits,use_special)
    st.write(f"Generated Password: {password}")


st.write("--------------------------------")

st.write("Made with ❤️ by [Taha Awan]")
