import streamlit as st
st.set_page_config(page_title="The One & Only", page_icon=":)", layout="centered")
)
st.markdown(
   """
<style>
   /* Full-page gradient background */
   html, body, .stApp {
       margin: 0;
       padding: 0;
       height: 100%;
       width: 100%;
       overflow: hidden;
       background: linear-gradient(135deg, #fff9c4, #fff3e0, #fffde7);
       background-size: 400% 400%;
       animation: gradientBG 15s ease infinite;
       position: relative;
   }
   @keyframes gradientBG {
       0% {background-position: 0% 50%;}
       50% {background-position: 100% 50%;}
       100% {background-position: 0% 50%;}
   }
   /* Remove extra Streamlit padding */
   .css-1d391kg, .css-1v3fvcr {margin:0; padding:0; height:100%;}
   /* Block container */
   .block-container {padding-top:20px !important; z-index:2; position:relative;}
   /* Hide Streamlit menu/footer */
   #MainMenu {visibility:hidden;}
   footer {visibility:hidden;}
   /* Title and message */
   h1 {color:#ff69b4; text-align:center; font-family:'Comic Sans MS', cursive, sans-serif; position:relative; z-index:2;}
   h2 {color:#ff1493; text-align:center; font-family:'Arial', sans-serif; position:relative; z-index:2;}
   /* Button style */
   .stButton>button {background-color:#ffb6c1; color:white; font-size:20px; border-radius:10px; padding:10px 24px; z-index:2; position:relative;}
   /* Floating upright hearts */
   .heart {
       position: absolute;
       width: 15px;
       height: 15px;
       background: #ff6f91;
       opacity: 0.7;
       border-radius: 50% 50% 0 0;
       transform: rotate(0deg);  /* upright */
       animation: floatUp 6s linear infinite;
   }
   .heart:before,
   .heart:after {
       content:"";
       position:absolute;
       width:15px;
       height:15px;
       background:#ff6f91;
       border-radius:50%;
   }
   .heart:before { top: -7.5px; left:0; }  /* left lobe */
   .heart:after { top: -7.5px; left:7.5px; } /* right lobe */
   @keyframes floatUp {
       0% { transform: translateY(100vh); opacity:0.7; }
       50% { opacity:1; }
       100% { transform: translateY(-20vh); opacity:0; }
   }
</style>
<!-- Floating hearts at different horizontal positions -->
<div class="heart" style="left:10%; animation-delay:0s;"></div>
<div class="heart" style="left:25%; animation-delay:1s;"></div>
<div class="heart" style="left:40%; animation-delay:2s;"></div>
<div class="heart" style="left:60%; animation-delay:3s;"></div>
<div class="heart" style="left:75%; animation-delay:4s;"></div>
<div class="heart" style="left:90%; animation-delay:5s;"></div>
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
