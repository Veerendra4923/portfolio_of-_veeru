import  streamlit as st
import send_email as se
st.header("Contact")
with st.form(key='form'):
    x=st.text_input('Enter your email address')
    y=st.text_area("Enter the message")

    ms=f"""\
subject: New Message from {x}

from: {x}
{y}
"""
    z = st.form_submit_button('Submit')

    if z:
        se.send_emailo(ms)
        st.info('Your email has been sent sucessfully!')
