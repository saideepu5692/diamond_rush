import streamlit as st
import pyrebase
import json
from PIL import Image
import base64

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
        st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
        # Define sidebar contents
        with st.sidebar:
            # Add profile icon1fNx44o_jGdQ_WALqYjo_nylaH02yrPx8
            st.markdown("<div style='text-align: center'><img src='https://drive.google.com/uc?export=view&id=1fNx44o_jGdQ_WALqYjo_nylaH02yrPx8' width='100'></div>", unsafe_allow_html=True)
            # Add text
            st.markdown("## Hello!, Welcome to Diamond Rush")
            st.markdown("Here you can solve the exciting treasure hunt")

        # Define the CSS style
        style = """
        <style>
            .columnImage {
                box-sizing: border-box;
                float: left;
                width: 107%;
            }
        </style>
        """

        # Add the CSS style to the page
        st.markdown(style, unsafe_allow_html=True)

        # Define the columns
        col1, col2, col3 = st.columns(3)
        col4, col5, col6 = st.columns(3)
        col7, col8, col9 = st.columns(3)

        # Add content to each column
        with col1:
            st.markdown(f"""<a href="page1"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=1z59GvMgWiFOSJGRF9wP_qL9urclIuv9o"></a>""",unsafe_allow_html=True)
        with col2:
            st.markdown(f"""<a href="www.google.com"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=1iDPB9zJWc_jFErSQV6eFXp4JRU47t1vu"></a>""",unsafe_allow_html=True)
        with col3:
            st.markdown(f"""<a href="www.google.com"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=13JqXqmJGadtkASS8oKkRpncxyCXnl9XU"></a>""",unsafe_allow_html=True)
        with col4:
            st.markdown(f"""<a href="www.google.com"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=1HmIbxSlXSCit8qJ9VGvLpmbKgutqmZ8F"></a>""",unsafe_allow_html=True)
        with col5:
            st.markdown(f"""<a href="www.google.com"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=1gdakk6gwfVa-0Qw_f-Sitp4zLB8BoiiX"></a>""",unsafe_allow_html=True)
        with col6:
            st.markdown(f"""<a href="www.google.com"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=1Z_bX1lyfaB4JraiUQ9vX8lh4-ao8_Qki"></a>""",unsafe_allow_html=True)
        with col7:
            st.markdown(f"""<a href="page1"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=11bUMmqlRJRDsWbfjkwqaD3--jv-DwkKo"></a>""",unsafe_allow_html=True)
        with col8:
            st.markdown(f"""<a href="page2"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=12dSWYJO9didCNBMOAoTZkCUlHNFqffB3"></a>""",unsafe_allow_html=True)
        with col9:
            st.markdown(f"""<a href="www.google.com"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=13UvmRI3tpKTF0B8KKvYJE7nLmGwSYbn2"></a>""",unsafe_allow_html=True)
# Run the app
if __name__ == "__main__":
    main()
