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
# Add the text to the webpage
text = "While going forward, Bhargav sees an oldman walking with a BLUE STICK and asks if he knew anything about a diamond treasure in this town. The oldman and Bhargav are facing opposite to each other. Seeing the sunset directly, the old man starts remembering something and speaks back. The old man's reply is in the form of audio file below. Listen it carefully and answer the question."
question="In what direction should Bhargav go now? Please answer in terms on option number only(1 or 2 or 3 or 4)"
option1="1.In the same direction he is facing now"
option2="2.Opposite direction to the direction he is facing now"
option3="3.Left to the direction he is facing now"
option4="4.Right to the direction he is facing now"



# Define the audio file to play
st.header("The Oldman")
st.write(text)
st.write(question)
st.write(option1)
st.write(option2)
st.write(option3)
st.write(option4)
answer2 = st.text_input("Enter your answer here",key="abc")
st.write("Clue:")
response = requests.get("https://raw.githubusercontent.com/saideepu5692/diamond_rush/main/support/audio_file.mp3")
st.audio(response.content, format='audio/mp3')

# Get a Firestore client
db = firestore.client()
db.collection('my_collection').document(st.session_state.get('uid')).update({"answer2":answer2})

if(answer2=='1'):
    st.write("Correct! Go along the road to find new hint")
else:
    st.write("Wrong!Go to map page and try again")
