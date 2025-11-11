import streamlit as st
st.set_page_config(page_title="The One & Only", page_icon=":)", layout="centered")
# CSS to shift content up

st.markdown(

    """
<style>

    /* Move Streamlit main block up */

    .appview-container .main {

        padding-top: 50px;  /* decrease this number to move further up */

    }

    /* Optional: gradient background */

    body {

        background: linear-gradient(135deg, #FFD1DC, #FFE7BA, #D1FFFC, #D1FFC4, #FFD1FC);

        background-size: 400% 400%;

        animation: gradientBG 15s ease infinite;

    }

    @keyframes gradientBG {

        0% {background-position: 0% 50%;}

        50% {background-position: 100% 50%;}

        100% {background-position: 0% 50%;}

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
