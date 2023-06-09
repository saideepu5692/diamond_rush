import streamlit as st
from io import BytesIO
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
data={}
if not firebase_admin._apps:
        # Replace GITHUB_RAW_URL with the raw URL of your .json file in your GitHub repository
        response = requests.get("https://raw.githubusercontent.com/saideepu5692/diamond_rush/main/support/diamond-rush-0808-firebase-adminsdk-fm0jo-2d5090e23a.json")
        json_content = response.json()
        cred = credentials.Certificate(json_content)
        firebase_admin.initialize_app(cred)
# Define the text to display
text = "Once upon a time, there lived a young man named Bhargav. He was very curious in doing adventures. On a fine day, he happened to notice a book named ""The Diamond Grimore"" when he was cleaning his Attic. The book revealed about a hidden treasure , a large diamond to be specific. When his eye spotted the author of book, he was astonished! It was none other than VIKRAMACHARYA, his Grandfather!! Bhargav's father used to tell him that his grandfather was a very wealthy man with some big secrets. Deep inside, Bhargav felt a hunch that there was some legacy left by his grandfather at the other end of this book. So Curiously, he opened the book and there was an Image attached to the 1st page. Due to papermites, the image's quality has been compromised.Help him retrieve the details present in that image"
question="What is the address specified in the image?"
st.session_state["authenticated"] = True
# Define the audio file to play
st.header("The Diamond Grimore")
st.write(text)
st.write(question)

# Create the input box for the user to enter their answer
answer1 = st.text_input("Enter your answer here")
# Add the text to the webpage
if(answer1):
    if(answer1=='629 Lakeview Drive'):
        st.write("Correct! Go along the road to find new hint")
    else:
        st.write("Wrong!Go to map page and try again")
st.write("Clue")
#image = Image.open(r'C:\Users\barga\Streamlit_run\pages\hint_image_1.jpg')
#st.markdown("<div style='text-align: center'><img src='https://drive.google.com/uc?export=view&id=1eoja7u80xJMDSUGCRkYtQvgT8AaoLkN-' width='100'></div>", unsafe_allow_html=True)

st.image("https://drive.google.com/uc?export=view&id=1eoja7u80xJMDSUGCRkYtQvgT8AaoLkN-")
# Store a variable in Firebase
#st.write(eval(str(db[0])))
#st.write(eval(db))
db = firestore.client()
db.collection('my_collection').document(st.session_state.get('uid')).update({"answer1":answer1})

