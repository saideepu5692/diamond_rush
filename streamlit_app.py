import streamlit as st
import json
import firebase_admin
from firebase_admin import credentials,auth, firestore
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

# Initialize Firebase app
response = requests.get("https://raw.githubusercontent.com/saideepu5692/diamond_rush/main/support/diamond-rush-0808-firebase-adminsdk-fm0jo-2d5090e23a.json")
json_content = response.json()
cred = credentials.Certificate(json_content)
firebase_admin.initialize_app(cred)
db = firestore.client()

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
