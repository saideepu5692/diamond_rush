import streamlit as st
import os
import firebase_admin
from firebase_admin import credentials, firestore
import webbrowser
from PIL import Image
import requests
if not firebase_admin._apps:
        # Replace GITHUB_RAW_URL with the raw URL of your .json file in your GitHub repository
        response = requests.get("https://raw.githubusercontent.com/saideepu5692/diamond_rush/main/support/diamond-rush-0808-firebase-adminsdk-fm0jo-2d5090e23a.json")
        json_content = response.json()
        cred = credentials.Certificate(json_content)
        firebase_admin.initialize_app(cred)
params = st.experimental_get_query_params()

# Access the parameter values by key
st.session_state['uid'] = params.get('uid')[0]
answer51=""
answer52=""
answer53=""
answer54=""


# Define the text to display
text="The Stranger said,'You did very well! You have earned my respect. GO RIGHT to find what you are looking for!'. Bhargav thanked him and went on to continue his journey. He entered a cave which was very dark. Tired because of journey, he decided to rest. Suddenly he felt something moving. He turned on his Mobile's Flashlight to find something very dangerous. The cave has its walls attached with spikes!! And the worst part is it is slowly closing in!! Now answer the below questions as fast as possible. Each question you answer gives Bhargav an energy bar which helps him go to other end of cave from where he can exit safely. If you do not answer the question properly, the cave might close in and destroy everything including Bhargav in it!!Clock is Ticking!"
# Define the image file to play
st.header("The Climax")
st.write(text)

question51="What was the name of Bhargav's Grandfather?"
st.write(question51)
answer51=st.text_input("Enter your answer here", key="hint51")
if(answer51):
    question52="What was the color of the stick the Oldman was using?"
    st.write(question52)
    answer52=st.text_input("Enter your answer here", key="hint52")
    if(answer52):
        question53="Is the girl who was murdered a married person?"
        st.write(question53)
        answer53=st.text_input("Enter your answer here", key="hint53")
        if(answer53):
            question54="How many people were there in total in the Attention to detail video?"
            st.write(question54)
            answer54=st.text_input("Enter your answer here", key="hint54")
            if(answer54):
                st.write("You have entered your input. please return to main page")
    
db = firestore.client()
db.collection('my_collection').document(st.session_state.get('uid')).update({"answer51":answer51,"answer52":answer52,"answer53":answer53,"answer54":answer54})

        


