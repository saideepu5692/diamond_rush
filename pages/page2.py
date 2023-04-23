import streamlit as st
import os
from io import BytesIO
import firebase_admin
from firebase_admin import credentials, firestore
import webbrowser
import requests
import json
from PIL import Image
import requests
import json
# Get the query parameters from the current URL
params = st.experimental_get_query_params()

# Access the parameter values by key
st.session_state['uid'] = params.get('uid')[0]
if not firebase_admin._apps:
        # Replace GITHUB_RAW_URL with the raw URL of your .json file in your GitHub repository
        response = requests.get("https://raw.githubusercontent.com/saideepu5692/diamond_rush/main/support/diamond-rush-0808-firebase-adminsdk-fm0jo-2d5090e23a.json")
        json_content = response.json()
        cred = credentials.Certificate(json_content)
        firebase_admin.initialize_app(cred)
# Create the input box for the user to enter their answer
answer2 = st.text_input("Enter your answer here",key="abc")
# Add the text to the webpage

st.write("Clue:")
response = requests.get("https://raw.githubusercontent.com/saideepu5692/diamond_rush/main/support/audio_file.mp3")
st.audio(response.content, format='audio/mp3')

# Get a Firestore client
db = firestore.client()
db.collection('my_collection').document(st.session_state.get('uid')).update({"answer2":answer2})

if(answer2):
    st.write("You have entered your input. please return to main page by clicking below button")
    st.markdown(f"""<a href="/login?uid={st.session_state.get('uid')}" target="_self"><button>Go to map</button></a>""", unsafe_allow_html=True)
        


