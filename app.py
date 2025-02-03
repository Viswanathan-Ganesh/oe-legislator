import streamlit as st


st.set_page_config(page_title="OE QNA", page_icon=":passenger_ship:", layout="centered")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

contact_form = """
    <form action="https://formsubmit.co/viswanathanganesh24@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <textarea name="message" placeholder="Your Query" required></textarea>
        <button type="submit" alignment="center">Send</button>
    </form>
"""


st.markdown("""
    <style>
    [data-testid="stImage"] {
        text-align: center;
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 30%;
    }
    </style>
    """, unsafe_allow_html=True)

with st.container():
    st.image("IIT_Madras_Logo.svg.png", use_container_width=True)
    st.markdown("<h2 style='text-align: center; font-weight: bold;'>QNA of Department of Ocean Engineering</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Please write any queries or concerns regarding your academics and non-academic things here. This is sent directly to the OE Legislator</p>", unsafe_allow_html=True)
    st.markdown(contact_form, unsafe_allow_html=True)
    st.write("<p></p>", unsafe_allow_html=True)
    st.write(f"<p style='text-align: center;'>Made with <3 by Viswanathan Ganesh, NA23B077</p>", unsafe_allow_html=True)



