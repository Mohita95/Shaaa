import streamlit as st
st.set_page_config(page_title="The One & Only", page_icon=":)", layout="centered")
)
st.markdown(
   """
<style>
   /* Full-page gradient background */
   html, body, .stApp {
       height: 100%;
       margin: 0;
       padding: 0;
       background: linear-gradient(135deg, #fff9c4, #fff3e0, #fffde7);
       background-size: 400% 400%;
       animation: gradientBG 15s ease infinite;
       overflow: hidden; /* prevent scrollbars from hearts */
   }
   @keyframes gradientBG {
       0% {background-position: 0% 50%;}
       50% {background-position: 100% 50%;}
       100% {background-position: 0% 50%;}
   }
   /* Shift main content up */
   .block-container {
       padding-top: 20px;  /* smaller = higher */
       padding-bottom: 20px;
       position: relative;
       z-index: 2;  /* make content appear above hearts */
   }
   /* Hide Streamlit menu & footer */
   #MainMenu {visibility: hidden;}
   footer {visibility: hidden;}
   /* Title style */
   h1 {
       color: #ff69b4;
       text-align: center;
       font-family: 'Comic Sans MS', cursive, sans-serif;
       z-index: 2;
       position: relative;
   }
   /* Message style */
   h2 {
       color: #ff1493;
       text-align: center;
       font-family: 'Arial', sans-serif;
       z-index: 2;
       position: relative;
   }
   /* Button style */
   .stButton>button {
       background-color: #ffb6c1;
       color: white;
       font-size: 20px;
       border-radius: 10px;
       padding: 10px 24px;
       z-index: 2;
       position: relative;
   }
   /* Floating hearts */
   .heart {
       position: absolute;
       width: 15px;
       height: 15px;
       background: #ff6f91;
       opacity: 0.7;
       transform: rotate(45deg);
       animation: floatUp 6s linear infinite;
   }
   .heart:before,
   .heart:after {
       content: "";
       position: absolute;
       width: 15px;
       height: 15px;
       background: #ff6f91;
       border-radius: 50%;
   }
   .heart:before { top: -7.5px; left: 0; }
   .heart:after { left: 7.5px; top: 0; }
   @keyframes floatUp {
       0% { transform: translateY(100vh) rotate(45deg); opacity: 0.7; }
       50% { opacity: 1; }
       100% { transform: translateY(-20vh) rotate(45deg); opacity: 0; }
   }
</style>
<!-- Create multiple floating hearts -->
<div class="heart" style="left: 10%; animation-delay: 0s;"></div>
<div class="heart" style="left: 30%; animation-delay: 2s;"></div>
<div class="heart" style="left: 50%; animation-delay: 4s;"></div>
<div class="heart" style="left: 70%; animation-delay: 1s;"></div>
<div class="heart" style="left: 90%; animation-delay: 3s;"></div>
   """,
   unsafe_allow_html=True
)
 
st.title("This is for My Forever Baby, Shaa<3  \nSmile karo pehle, Koi baat nahi Fake bhi chalegi :) \n")
st.write("Now click the button below thinking about all your Powers!!!")
if st.button("Works For Greek Gods Only"):
   st.image("https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif", use_container_width=True)
   st.markdown(
       "<h2 style='text-align:center; color:#ff69b4;'>Mera Shaa, Tu jaldi theek hogaaaa! :) </h2>",
       unsafe_allow_html=True
   )
