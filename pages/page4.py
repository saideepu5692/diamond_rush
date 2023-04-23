import streamlit as st
import os
import firebase_admin
from firebase_admin import credentials, firestore
import webbrowser
from PIL import Image
import requests


# Define the text to display
text="The Demon said ,'Very well! You solved the puzzle correctly. Go forward with your adventure young man!' Bhargav continued his journey He came across a young man, telling he knew where the treasure was! When Bhargav asked him about the details, he said,'My friend! I will give you the right direction you need to go to find that treasure. But, I want to test your attention to detail. Let's see what you can do.'"
question=" Help Bhargav win this puzzle so that he can finally know the location of treasure."
question2="Watch the video and aswer the questions in form of L,R,M. Here, L stands for 'Left Person', R stands for 'Right Person' and M stands for 'Middle Person'. There will be 3 questions in video. After watching it, Type your answer in answerbox.(Final answer in answer box should be like, LRM or RRM etc.)"
# Define the image file to play
st.header("The Stranger")
st.write(text)
st.write(question)
st.write(question2)

# Create the input box for the user to enter their answer
# Add the text to the webpage

st.write("Clue:")
#video_file = open(r'C:\Users\saide\OneDrive\Desktop\vs\video_hint4.mp4', 'rb')
#video_bytes = video_file.read()
response = requests.get("https://raw.githubusercontent.com/saideepu5692/diamond_rush/main/support/video_hint4.mp4")
st.video(response.content)
answer4 = st.text_input("Enter your answer here", key="hint4")

# Get a Firestore client
db = firestore.client()
db.collection('my_collection').document(st.session_state.get('uid')).update({"answer4":answer4})


if(answer4):
    st.write("You have entered your input. please return to main page by clicking below button")
    st.markdown(f"""<a href="/login?uid={st.session_state.get('uid')}" target="_self"><button>Go to map</button></a>""", unsafe_allow_html=True)
        


