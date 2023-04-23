import streamlit as st
import os
import firebase_admin
from firebase_admin import credentials, firestore
import webbrowser
from PIL import Image
import requests
from io import BytesIO

data={}

# Initialize a Firebase app
if not firebase_admin._apps:
    # Replace GITHUB_RAW_URL with the raw URL of your .json file in your GitHub repository
    response = requests.get('https://github.com/saideepu5692/diamond_rush/blob/1187a93ad1140796b0010fbf7e28075fffb2260b/support/diamond-rush-0808-firebase-adminsdk-fm0jo-2d5090e23a.json')
    cred = credentials.Certificate(BytesIO(response.content))
    firebase_admin.initialize_app(cred)



# Define the text to display
text = "Once upon a time, there lived a young man named Bhargav. He was very curious in doing adventures. On a fine day, he happened to notice a book named ""The Diamond Grimore"" when he was cleaning his Attic. The book revealed about a hidden treasure , a large diamond to be specific. When his eye spotted the author of book, he was astonished! It was none other than VIKRAMACHARYA, his Grandfather!! Bhargav's father used to tell him that his grandfather was a very wealthy man with some big secrets. Deep inside, Bhargav felt a hunch that there was some legacy left by his grandfather at the other end of this book. So Curiously, he opened the book and there was an Image attached to the 1st page. Due to papermites, the image's quality has been compromised.Help him retrieve the details present in that image"
question="What is the address specified in the image?"




# Define the audio file to play
st.header("The Diamond Grimore")
st.write(text)
st.write(question)



# Create the input box for the user to enter their answer
answer1 = st.text_input("Enter your answer here")
# Add the text to the webpage
st.write("Clue")
#image = Image.open(r'C:\Users\barga\Streamlit_run\pages\hint_image_1.jpg')
#st.markdown("<div style='text-align: center'><img src='https://drive.google.com/uc?export=view&id=1eoja7u80xJMDSUGCRkYtQvgT8AaoLkN-' width='100'></div>", unsafe_allow_html=True)

st.image("https://drive.google.com/uc?export=view&id=1eoja7u80xJMDSUGCRkYtQvgT8AaoLkN-")
db = firestore.client()

# Store a variable in Firebase
db.collection('my_collection').document('my_document').set({"answer1":answer1})

if(answer1):
    st.write("You have entered your input. please return to main page by clicking below button")
    if st.button("Go to map"):
        webbrowser.open("https://www.amazon.in")
