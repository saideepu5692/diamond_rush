Project Name: Diamond Rush

Time taken to complete the project: 7 days

Project Description: This interactive treasure hunt game consists of clues and hints in which the softskills of the user(such as Eye for detail, attentiveness etc) are tested.
The project details are as follows:
    1) Clue 1: It examines the capability to the user to see things differently and remember what he saw. As it is the first hint, inorder to make game interesting, the difficulty level is easy.
    2)Clue 2: The audio file in this clue tests the attentiveness of the user and his capability to solve something even without a visual help. It can also comprehend the user's understanding ability of the language.
    3)Clue 3: This clue also tests the lateral thinking and out of the box thinking ability of the user. It can also tell how strong the user is, in visual remembering.
    4)Clue 4: This clue tests the creative thinking and the ability of the user to observe small things in a detailed manner.
    5)Clue 5: This clue tests the attentiveness of the user. It also determines the ability of the user to work under clock pressure.

NOTE: Please click on images along road in the main page's map to go forward into story. All your inputs will be be stored and your score will be evaluated beased on your inputs.
    
Number of Solutions: 1
  Solution: When the user enters all answers correctly even in last hint page, the game is Completed.
Number of Deadends: 4
  Deadend: In each clue page, if there is a wrong answer given, it leads to deadends as shown in the map in main page.
Steps to setup the project:
  1) Download the zipfile by going to 'Code' and then click on 'Download ZIP'.
  2) Now, extract the zip file using Winrar or 7zip.
  3) After this, open any IDE like, Visual Studio Code.
  4) Add the downloaded files into a folder and add that folder in explorer of VSCode.
  5) Install the necessary requirements such as Python, Streamlit, firebase_admin, pandas.(To install Streamlit/firebase/pandas, you need to run pip install streamlit/pandas/firebase-admin)
  6) Now, run streamlit_app.py
  7) To view the file as website, open cmd and type 'python -m streamlit run 'path of the file''
  8) You will be redirected to a login page.
  9) Login/Signup to start playing the game.
NOTE: For ADMIN USER, please enter the ADMIN EMAIL ID AND ADMIN PASSWORD to track the results of users.

//Implemented Features//
  1.Anyone with an email address can create an Id and password to participate in the game
  2.The puzzle contains:
        a)5 clues
        b)4 dead-ends
        c)1 solution 
        d)All the progress / user data (eg - time taken by each user for every step, solution accuracy, etc.) depending on your puzzle requirements should be stored for every user
        e)On refreshing, from either browser or website, the puzzle should start from the same step or give the user an option to restart
        f)A dashboard for the admin where the progress of all the users can be tracked & analyzed
        g) A sidebar consisting the account details of user.
//Additional Features//
  1.User Analytics are stored in admin dashboard
  2.User Leaderboard
