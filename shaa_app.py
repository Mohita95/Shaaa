import streamlit as st
st.set_page_config(page_title="The One & Only", page_icon=":)", layout="centered")
# CSS to color the whole page
st.markdown(
   """
<style>
   /* Full-page background including top */
   .stApp, .css-1d391kg, .css-1v3fvcr {
       background: linear-gradient(135deg, #fff9c4, #fff3e0, #fffde7);
       background-size: 400% 400%;
       animation: gradientBG 15s ease infinite;
   }
   @keyframes gradientBG {
       0% {background-position: 0% 50%;}
       50% {background-position: 100% 50%;}
       100% {background-position: 0% 50%;}
   }
   /* Shift main content up */
   .block-container {
       padding-top: 20px;  /* smaller = higher up */
       padding-bottom: 20px;
   }
   /* Hide Streamlit menu & footer (optional) */
   #MainMenu {visibility: hidden;}
   footer {visibility: hidden;}
   /* Title style */
   h1 {
       color: #ff69b4;
       text-align: center;
       font-family: 'Comic Sans MS', cursive, sans-serif;
   }
   /* Message style */
   h2 {
       color: #ff1493;
       text-align: center;
       font-family: 'Arial', sans-serif;
   }
   /* Button style */
   .stButton>button {
       background-color: #ffb6c1;  
       color: white;
       font-size: 20px;
       border-radius: 10px;
       padding: 10px 24px;
   }
</style>
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
