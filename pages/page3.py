import streamlit as st
import os
import firebase_admin
from firebase_admin import credentials, firestore
import webbrowser
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
# Define the text to display
text = "Suddenly, the sky was getting dark. A black cloud appeared in sky. A voice whispered from the sky. You have chosen the wrong route you weakling! Many have walked this way and all of them have perished! Let's test whether you are worthy to findout what is on the other side of your adventure. I will let you go if you answer my question correctly. If not, I shall take your life!"
question=" Tell me whether the girl died by Suicide or Murder in this photo."
question2="Help Bhargav investigate the photo and answer the correct option number in answer box.(Answer should be 1 or 2)"
option1="1.Suicide"
option2="2.Murder"

# Define the image file to play
st.header("The Demon")
st.write(text)
st.write(question)
st.write(question2)
st.write(option1)
st.write(option2)

# Create the input box for the user to enter their answer
answer3 = st.text_input("Enter your answer here", key="hint3")
# Add the text to the webpage

st.write("Clue:")
#response = requests.get("https://raw.githubusercontent.com/saideepu5692/diamond_rush/main/support/image_hint3.jpg")
#st.write(response.text)
#image=Image.open(r'{response.content}')
st.image("https://raw.githubusercontent.com/saideepu5692/diamond_rush/main/support/image_hint3.jpg")
#st.image("support/image_hint3.jpg")
# Get a Firestore client
db = firestore.client()
db.collection('my_collection').document(st.session_state.get('uid')).update({"answer3":answer3})
if(answer3):
    if(answer3=='2'):
        st.write("Correct! Go along the road to find new hint")
    else:
        st.write("Wrong!Go to map page and try again")

