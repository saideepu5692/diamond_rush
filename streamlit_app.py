import streamlit as st
import json
import firebase_admin
from firebase_admin import credentials, auth
from PIL import Image
import requests
import pandas as pd
import datetime

# Set Streamlit page config
st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":guardsman:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

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

# Define the login page
def login():
    st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
    st.header("Welcome to Diamond Rush!")

    email = st.text_input("Email", key="login-email")
    password = st.text_input("Password", type="password", key="login-password")
    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            expiration_time = datetime.datetime.now() + datetime.timedelta(hours=1)
            st.experimental_set_query_params(authenticated=True, uid=user["localId"], expires=expiration_time)
        except:
            st.error("Authentication failed. Please check your credentials and try again.")
    if st.button("Sign Up"):
        st.session_state['signup'] = True
    if st.button("Forgot Password?"):
        st.session_state['forgot_password'] = True

# Define the Home page
def Home():
    st.header("Welcome to Diamond Rush - Home")
    # Your Home page content goes here

# Define the Admin page
def admin():
    st.header("Admin Page")
    # Your admin page content goes here

# Define the main page
def main():
    params = st.experimental_get_query_params()
    if "expires" in params and datetime.datetime.now() < datetime.datetime.fromisoformat(params["expires"][0]):
        st.session_state.authenticated = True
        st.session_state.uid = params["uid"][0]

    if "admin" in st.session_state:
        admin()
    elif "authenticated" in st.session_state and st.session_state.authenticated:
        Home()
    else:
        login()

# Run the app
if __name__ == "__main__":
    main()
