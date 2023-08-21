import streamlit as st
import json
from PIL import Image
import firebase_admin
from firebase_admin import credentials, auth
import requests
import tempfile
import pandas as pd
st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":guardsman:",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.header("Welcome to Diamond Rush!")
# Fetch Firebase credentials JSON from GitHub
credentials_url = "https://raw.githubusercontent.com/saideepu5692/diamond_rush/main/support/diamond-rush-0808-firebase-adminsdk-fm0jo-2d5090e23a.json"
response = requests.get(credentials_url)
json_content = response.json()

# Check if the Firebase app is already initialized
if not firebase_admin._apps:
    # Create a temporary file to write the JSON content
    temp_json_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    temp_json_file.write(response.content)
    temp_json_file.close()

    # Initialize Firebase SDK
    cred = credentials.Certificate(temp_json_file.name)
    firebase_admin.initialize_app(cred)

    st.write("Firebase SDK initialized successfully!")

    # Clean up temporary file
    temp_json_file.unlink()
else:
    st.write("Firebase SDK is already initialized!")

# Rest of your Streamlit app code

# Streamlit UI for login page
st.title("Login Page")

# User input fields
username = st.text_input("Enter Username")
password = st.text_input("Enter Password", type="password")

# Sign-in button
login_button = st.button("Sign In")

# Create user button
create_user_button = st.button("Create User")

# Forgot password button
forgot_password_button = st.button("Forgot Password")

# Create a session state dictionary to store session-related information
if "session_state" not in st.session_state:
    st.session_state.session_duration = 3600  # 1 hour in seconds
    st.session_state.logged_in = False
    st.session_state.is_admin = False

# Login function
def login(email, password):
    try:
        user = firebase_admin.auth.get_user_by_email(email)
        auth_user = firebase_admin.auth.verify_password_reset_code(password)
        if auth_user.uid == user.uid:
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.success("Login successful!")
            # Redirect to the home page with images
        else:
            st.error("Invalid credentials.")
    except firebase_admin.auth.AuthError as e:
        if "USER_NOT_FOUND" in str(e):
            st.error("User does not exist.")
        else:
            st.error("Invalid credentials.")

# Create user function
def create_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        st.success("User created successfully!")
    except Exception as e:
        if "EMAIL_EXISTS" in str(e):
            st.error("Email already exists.")
        else:
            st.error("Failed to create user.")

# Forgot password function
def forgot_password(email):
    try:
        auth.generate_password_reset_link(email)
        st.success("Password reset link sent to your email.")
    except Exception as e:
        if "USER_NOT_FOUND" in str(e):
            st.error("User does not exist.")
        else:
            st.error("Failed to send reset link.")

# Handle button clicks
if create_user_button:
    create_user(username, password)

if forgot_password_button:
    forgot_password(username)

if login_button:
    login(username, password)

# If user is logged in, display home page
if st.session_state.logged_in:
    # If user is admin, display admin page
    if st.session_state.is_admin:
        st.success("Welcome, Admin!")
        # Add logic for displaying admin-specific functionality
    else:
        st.success("Welcome")
        # Add logic for displaying home page with images
