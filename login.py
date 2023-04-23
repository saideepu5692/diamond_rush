import streamlit as st
import pyrebase
import json
from PIL import Image
import base64

# Define a function to check if the login is valid
def authenticate(username, password):
    # Replace this with your authentication logic
    if username == "user" and password == "password":
        return True
    else:
        return False

# Define the login page
def login():
    firebaseConfig = {
        # Add your Firebase configuration details here
        'apiKey': "AIzaSyBaP-ig_zlk7o5ixfg2NVDoSlaSuHfZCV0",
    'authDomain': "diamond-rush-0808.firebaseapp.com",
    'projectId': "diamond-rush-0808",
    'storageBucket': "diamond-rush-0808.appspot.com",
    'messagingSenderId': "519582232920",
    'appId': "1:519582232920:web:a579fdbd905bcedb57752d",
    'measurementId': "G-GHXB2SQLBF",
    'databaseURL': ""
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    db = firebase.database()
    def login_page():
        email = st.text_input("Email", key="login-email")
        password = st.text_input("Password", type="password", key="login-password")
        if st.button("Login"):
            try:
                # Authenticate the user's credentials
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state["authenticated"] = True
                #s.experimental_rerun()
                # Redirect to the main page
                # Or display an error message if the credentials are incorrect
            except:
                st.error("Authentication failed. Please check your credentials and try again.")
        if st.button("Sign Up"):
            # Show the sign-up page
            st.session_state['signup'] = True
        if st.button("Forgot Password?"):
            # Show the forgot password page
            st.session_state['forgot_password'] = True

    # Define the sign-up page layout
    def signup_page():
        st.write("# Sign Up")
        new_email = st.text_input("Email", key="signup-email")
        new_password = st.text_input("Password", type="password", key="signup-password")
        if st.button("Create Account"):
            try:
                # Check if user already exists
                user = auth.get_user_by_email(new_email)
                st.error("Account creation failed. User already exists.")
            except:
                # Create a new user record in Firebase
                user = auth.create_user_with_email_and_password(new_email, new_password)
                #db.child("users").child(user["localId"]).set({"email": new_email})
                st.success("Account created successfully!")
                # Redirect to the login page
                st.session_state['signup'] = False
        if st.button("Back to Login"):
            # Show the login page
            st.session_state['signup'] = False
    # Define the forgot password page layout
    def forgot_password_page():
        st.write("# Forgot Password")
        forgot_email = st.text_input("Email", key="forgot-email")
        if st.button("Reset Password"):
            try:
                auth.send_password_reset_email(forgot_email)
                st.success("Password reset email sent!")
                # Redirect to the login page
                st.session_state['forgot_password'] = False
            except:
                st.error("Password reset failed. Please try again.")
        if st.button("Back to Login"):
            # Show the login page
            st.session_state['forgot_password'] = False
    if(st.session_state.get('signup')):
        # Show the sign-up page
        signup_page()
    elif(st.session_state.get('forgot_password')):
        # Show the forgot password page
        forgot_password_page()
    else:
        login_page()

# Define the main page
def main():
    # Check if the user is authenticated
    if ("authenticated" not in st.session_state or not st.session_state["authenticated"]):
        login()
    else:
        # Display the main page
        # Set common background image
        # Load image and convert to base64 string
        image = Image.open("diamond_rush.jpg")
        image_b64 = base64.b64encode(image.tobytes()).decode()
    
        st.image(image, caption="Your image", use_column_width=True)
        # Set common background image
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url('data:image/jpeg;base64,{image_b64}');
                background-size: cover;
                }}
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Create six containers
        col1, col2, col3 = st.columns(3)
        container1 = col1.container()
        container2 = col2.container()
        container3 = col3.container()

        col4, col5, col6 = st.columns(3)
        container4 = col4.container()
        container5 = col5.container()
        container6 = col6.container()

        # Add content to containers
        container1.write("Container 1")
        container2.write("Container 2")
        container3.write("Container 3")
        container4.write("Container 4")
        container5.write("Container 5")
        container6.write("Container 6")


# Run the app
if __name__ == "__main__":
    main()