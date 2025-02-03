import streamlit as st
import smtplib as s
import random as r

st.set_page_config(page_title="OE QNA", page_icon=":passenger_ship:", layout="centered")

pages = [] #icon=":passenger_ship:"

def smail_verification(smail):
    if smail[0:2] == "na" and smail.find("@smail.iitm.ac.in") != -1:
        mail =  st.secrets["email"]
        key = st.secrets["pass"]

        server = s.SMTP("smtp.gmail.com", 587)
        server.starttls()

        OTP = r.randrange(100000, 1000000)
        msg = f"Subject: {"Student Authentication"}\n\nHere is your OTP: {str(OTP)}"

        server.login(mail, password=key)
        try:
            server.sendmail(mail, smail, msg)
            return OTP
        except:
            return None
    else:
        return None

if "verified" not in st.session_state:
    st.session_state["verified"] = False

if "gotOtp" not in st.session_state:
    st.session_state["gotOtp"] = False 

if "otp" not in st.session_state:
    st.session_state["otp"] = 0

if st.session_state["verified"] == False and st.session_state["gotOtp"] == False:
    smail = st.text_input("Enter Smail: ", )
    submit = st.button("Get OTP")
    if submit:
        flag = smail_verification(smail)
        if flag == None:
            st.write("Invalid Email!")
        else:
            st.session_state["otp"] = flag
            st.session_state["gotOtp"] = True
        #st.session_state["verified"] = True
elif st.session_state["verified"] == False and st.session_state["gotOtp"] == True:
    user_otp = st.text_input("Enter OTP: ")
    verify = st.button("Verify")
    if verify:
        st.write(str(st.session_state["otp"]))
        print(st.session_state["otp"] == eval(user_otp))
        if (st.session_state["otp"] == eval(user_otp)):
            st.session_state["verified"] = True
        else:
            st.session_state["gotOtp"] = False
elif st.session_state["verified"] == True and st.session_state["gotOtp"] == True:
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




