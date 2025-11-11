import streamlit as st
st.set_page_config(
   page_title="The One & Only Shaa",
   page_icon="",
   layout="centered"
)
st.markdown("""
<style>
/* Full-page gradient background */
body, .stApp {
   background: linear-gradient(135deg, #fff9c4, #fff3e0, #fffde7);
   background-size: 400% 400%;
   animation: gradientBG 15s ease infinite;
   margin: 0;
   padding: 0;
   height: 100%;
   width: 100%;
}
@keyframes gradientBG {
   0% {background-position:0% 50%;}
   50% {background-position:100% 50%;}
   100% {background-position:0% 50%;}
}
/* Hide Streamlit menu/footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
/* Center content above hearts */
.centered-content {
   position: relative;
   z-index: 10;  /* above hearts */
   text-align: center;
   color: #ff1493;
   font-family: 'Comic Sans MS', cursive, sans-serif;
}
/* Button style */
.stButton>button {
   background-color:#ffb6c1;
   color:white;
   font-size:20px;
   border-radius:10px;
   padding:10px 24px;
   z-index: 10;
   position: relative;
}
/* Proper heart shape */
.heart {
   position: fixed;
   width: 20px;
   height: 20px;
   background: #ff6f91;
   transform: rotate(-45deg);
   top: 100vh; /* start below the page */
   z-index: 1;  /* behind content */
   opacity: 0.7;
   animation: floatUp 8s linear infinite; /* continuous looping */
}
.heart:before,
.heart:after {
   content:"";
   position:absolute;
   width: 20px;
   height: 20px;
   background: #ff6f91;
   border-radius: 50%;
}
.heart:before { top: -10px; left: 0; }
.heart:after { top: 0; left: 10px; }
/* Continuous float animation */
@keyframes floatUp {
   0% { transform: translateY(0) rotate(-45deg); opacity:0.7; }
   50% { opacity:1; }
   100% { transform: translateY(-200vh) rotate(-45deg); opacity:0; }
}
</style>
<!-- Floating hearts at different horizontal positions -->
<div class="heart" style="left:5%; animation-delay:0s;"></div>
<div class="heart" style="left:15%; animation-delay:2s;"></div>
<div class="heart" style="left:30%; animation-delay:4s;"></div>
<div class="heart" style="left:50%; animation-delay:1s;"></div>
<div class="heart" style="left:65%; animation-delay:3s;"></div>
<div class="heart" style="left:80%; animation-delay:5s;"></div>
<div class="heart" style="left:90%; animation-delay:0.5s;"></div>
""", unsafe_allow_html=True)
# Page content
st.markdown('<div class="centered-content">', unsafe_allow_html=True)
st.title("This is for My Forever Baby, Shaa<3\nSmile karo pehle, Koi baat nahi Fake bhi chalegi :)")
st.write("Now click the button below thinking about all your Powers!!!")
if st.button("Works For Greek Gods Only"):
   st.image("https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif", use_container_width=True)
   st.markdown("<h2>Mera Shaa, Tu jaldi theek hogaaaa! :) </h2>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
