import streamlit as st
import json
import pyrebase
from PIL import Image
import firebase_admin
from firebase_admin import credentials, firestore, auth
import requests
import pandas as pd
st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":guardsman:",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.header("Welcome to Diamond Rush!")
# Define a function to check if the login is valid
def authenticate(username, password):
    # Replace this with your authentication logic
    if username == "admin@gmail.com" and password == "diamondrush":
        return True
    else:
        return False

# Define the login page
def login():
    st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)

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
            if(authenticate(email,password)):
                st.session_state["admin"] = True
            else:
                try:
                    # Authenticate the user's credentials
                    user = auth.sign_in_with_email_and_password(email, password)
                    st.session_state["uid"]=user["localId"]
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
def admin():
    st.header("Admin Page")
    st.header("Leaderboard")
    if not firebase_admin._apps:
        # Replace GITHUB_RAW_URL with the raw URL of your .json file in your GitHub repository
        response = requests.get("https://raw.githubusercontent.com/saideepu5692/diamond_rush/main/support/diamond-rush-0808-firebase-adminsdk-fm0jo-2d5090e23a.json")
        json_content = response.json()
        cred = credentials.Certificate(json_content)
        firebase_admin.initialize_app(cred)
    db = firestore.client()
    uidd=[]
    answer1=[]
    answer2=[]
    answer3=[]
    answer4=[]
    answer51=[]
    answer52=[]
    answer53=[]
    answer54=[]
    email=[]
    # Extract data from Firestore database
    users_ref = db.collection("my_collection")
    for doc in users_ref.stream():
        data = doc.to_dict()
        answer1.append(data['answer1'])
        answer2.append(data['answer2'])
        answer3.append(data['answer3'])
        answer4.append(data['answer4'])
        answer51.append(data['answer51'])
        answer52.append(data['answer52'])
        answer53.append(data['answer53'])
        answer54.append(data['answer54'])
    docs = db.collection('my_collection').get()
    # Display the document names and email addresses in Streamlit
    for doc in docs:
        uid = doc.id
        user = auth.get_user(uid)
        email1= user.email 
        uidd.append(uid)
        email.append(email1)

    # Create a DataFrame from the inputs
    data = {'email':email,'answer1': answer1,'answer2':answer2,'answer3':answer3,'answer4':answer4,'answer51':answer51,'answer52':answer52,'answer53':answer53,'answer54':answer54,'uid':uidd}
    df = pd.DataFrame(data)
    st.table(df)
def Home():
    data={}
    # Initialize a Firebase app
    if not firebase_admin._apps:
        # Replace GITHUB_RAW_URL with the raw URL of your .json file in your GitHub repository
        response = requests.get("https://raw.githubusercontent.com/saideepu5692/diamond_rush/main/support/diamond-rush-0808-firebase-adminsdk-fm0jo-2d5090e23a.json")
        json_content = response.json()
        cred = credentials.Certificate(json_content)
        firebase_admin.initialize_app(cred)
    db = firestore.client()
    # Store a variable in Firebase
    db.collection('my_collection').document(st.session_state.get('uid')).set({'answer1':'NA','answer2':'NA','answer3':'NA','answer4':'NA','answer51':'NA','answer52':'NA','answer53':'NA','answer54':'NA'})
    st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
    # Define sidebar contents
    with st.sidebar:
        # Add profile icon1fNx44o_jGdQ_WALqYjo_nylaH02yrPx8
        st.markdown("<div style='text-align: center'><img src='https://drive.google.com/uc?export=view&id=1fNx44o_jGdQ_WALqYjo_nylaH02yrPx8' width='100'></div>", unsafe_allow_html=True)
        # Add text
        user = auth.get_user(st.session_state["uid"])
        email1= user.email
        st.markdown("## Hello!"+email1+", Welcome to Diamond Rush")
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
        st.markdown(f"""<div><img class="columnImage" src="https://drive.google.com/uc?export=view&id=1z59GvMgWiFOSJGRF9wP_qL9urclIuv9o"></div>""",unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<a href="page4?uid={st.session_state.get('uid')}"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=1iDPB9zJWc_jFErSQV6eFXp4JRU47t1vu"></a>""",unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<a href="page5?uid={st.session_state.get('uid')}"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=13JqXqmJGadtkASS8oKkRpncxyCXnl9XU"></a>""",unsafe_allow_html=True)
    with col4:
        st.markdown(f"""<div><img class="columnImage" src="https://drive.google.com/uc?export=view&id=1HmIbxSlXSCit8qJ9VGvLpmbKgutqmZ8F"></div>""",unsafe_allow_html=True)
    with col5:
        st.markdown(f"""<a href="page3?uid={st.session_state.get('uid')}"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=1gdakk6gwfVa-0Qw_f-Sitp4zLB8BoiiX"></a>""",unsafe_allow_html=True)
    with col6:
        st.markdown(f"""<div><img class="columnImage" src="https://drive.google.com/uc?export=view&id=1Z_bX1lyfaB4JraiUQ9vX8lh4-ao8_Qki"></div>""",unsafe_allow_html=True)
    with col7:
        st.markdown(f"""<a href="page1?uid={st.session_state.get('uid')}"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=11bUMmqlRJRDsWbfjkwqaD3--jv-DwkKo"></a>""",unsafe_allow_html=True)
    with col8:
        st.markdown(f"""<a href="page2?uid={st.session_state.get('uid')}"><img class="columnImage" src="https://drive.google.com/uc?export=view&id=12dSWYJO9didCNBMOAoTZkCUlHNFqffB3"></a>""",unsafe_allow_html=True)
    with col9:
        st.markdown(f"""<div><img class="columnImage" src="https://drive.google.com/uc?export=view&id=13UvmRI3tpKTF0B8KKvYJE7nLmGwSYbn2"></div>""",unsafe_allow_html=True)
# Define the main page
def main():
    # Check if the user is authenticated
    params = st.experimental_get_query_params()
    if(("authenticated" in st.session_state)or(params!={})):
        Home()
    elif("admin" in st.session_state):
        admin()
    else:
        # Display the main page
        # Set common background image
        # Load image and convert to base64 string
        login()


# Run the app
if __name__ == "__main__":
    main()
