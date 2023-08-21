import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase SDK
response = requests.get("https://raw.githubusercontent.com/saideepu5692/diamond_rush/main/support/diamond-rush-0808-firebase-adminsdk-fm0jo-2d5090e23a.json")
json_content = response.json()
cred = credentials.Certificate(json_content)
firebase_admin.initialize_app(cred)

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
        user = auth.get_user_by_email(email)
        auth_user = auth.verify_password_reset_code(password)
        if auth_user.uid == user.uid:
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.success("Login successful!")

            # Determine if the user is admin
            if email == "admin@example.com":  # Replace with actual admin email
                st.session_state.is_admin = True

            # Redirect to the home page with images
        else:
            st.error("Invalid credentials.")
    except auth.AuthError:
        st.error("Invalid credentials.")

# Create user function
def create_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        st.success("User created successfully!")
    except auth.AuthError:
        st.error("Failed to create user.")

# Forgot password function
def forgot_password(email):
    try:
        auth.generate_password_reset_link(email)
        st.success("Password reset link sent to your email.")
    except auth.AuthError:
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
