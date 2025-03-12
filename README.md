Password Generator & Strength Checker

Overview

This is a Streamlit web application that allows users to generate strong passwords and check the strength of their own passwords. It ensures security by verifying password length, the presence of special characters, uppercase letters, lowercase letters, and numbers.

Features

Password Generator: Generates a secure password based on user preferences.

Password Strength Checker: Evaluates password strength based on predefined security criteria.

Interactive UI: Built with Streamlit for an easy-to-use interface.



Installation

Make sure you have Python installed on your system. Then, follow these steps:

Clone this repository:

Install required dependencies:   pip install streamlit

Run the following command to start the Streamlit app:    streamlit run app.py


Usage

Adjust the slider to set the password length.

Check the boxes to include digits and special characters.

Click the Generate Password button to create a random password.

Enter a password in the Password Strength Checker field and click Check Strength to evaluate it.


Password Strength Criteria

A password is considered strong if it meets all of the following requirements:

Minimum 8 characters

At least one special character (!@#$%^&* etc.)

At least one uppercase letter (A-Z)

At least one lowercase letter (a-z)

At least one digit (0-9)

Technologies Used

Python

Streamlit

Random & String Modules

Author

Made with ❤️ by [Taha Awan]


