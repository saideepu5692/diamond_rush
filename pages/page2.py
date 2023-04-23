import streamlit as st
import os
import firebase_admin
from firebase_admin import credentials, firestore
import webbrowser
from page1 import db

# Initialize a Firebase app
if not firebase_admin._apps:
    cred = credentials.Certificate(r"C:\Users\saide\OneDrive\Desktop\vs\diamond-rush-0808-firebase-adminsdk-fm0jo-2d5090e23a.json")
    firebase_admin.initialize_app(cred)



# Define the text to display
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



# Create the input box for the user to enter their answer
answer2 = st.text_input("Enter your answer here")
# Add the text to the webpage

st.write("Clue:")
response = requests.get("https://raw.githubusercontent.com/saideepu5692/diamond_rush/main/support/audio_file.mp3")
st.audio(response.content, format='audio/mp3')

# Get a Firestore client

db.collection('my_collection').document(st.session_state.get('uid')).update({"answer2":answer2})

if(answer2):
    st.write("You have entered your input. please return to main page by clicking below button")
    if st.button("Go to map"):
        webbrowser.open("https://www.amazon.in")
        


