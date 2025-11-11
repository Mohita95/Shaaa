import streamlit as st
st.set_page_config(page_title="For Shaa", page_icon=":)", layout="centered")
st.title("Smile & Click — This is for My Forever Baby, Shaa <3")
st.write("Click the button below thinking about all your Powers!!!")
if st.button("Works For Greek Gods Only"):
   st.image("https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif", use_container_width=True)
   st.markdown(
       "<h2 style='text-align:center; color:#ff69b4;'>Mera Shaa, Tu jaldi theek hogaaaa! :) </h2>",
       unsafe_allow_html=True
   )
