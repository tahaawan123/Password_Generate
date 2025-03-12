import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    
    if use_special:
        characters += string.punctuation
    
    return ''.join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    if not password:
        return "Please enter a password!"
    if len(password) < 8:
        return "Weak 😔 (Minimum 8 characters required)"
    if not any(char in string.punctuation for char in password):
        return "Weak 😔 (Special character required)"
    if not any(char.isupper() for char in password):
        return "Weak 😔 (At least one capital letter required)"
    if not any(char.islower() for char in password):
        return "Weak 😔 (At least one lower letter required)"
    if not any(char.isdigit() for char in password):
        return "Weak 😔 (At least one digit required)"
    return "Strong 💪"

st.title("🔐 Password Generator & Strength Checker")

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
    password = generate_password(length, use_digits, use_special)
    strength = check_password_strength(password)
    
    st.write(f"Generated Password: `{password}`")
    st.write(f"Password Strength: {strength}")

st.write("--------------------------------")

st.subheader("🔎 Check Your Password Strength")
user_password = st.text_input("Enter your password to check strength", type="password")
if st.button("Check Strength"):
    if user_password:
        strength = check_password_strength(user_password)
        st.write(f"Password Strength: {strength}")
    else:
        st.write("⚠️ Please enter a password to check its strength.")

st.write("Made with ❤️ by [Taha Awan]")
