import streamlit as st
from database import Session, User
import bcrypt

def login():
    session = Session()
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        user = session.query(User).filter_by(username=username).first()
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
            return True, user.username
        else:
            st.error("Username/password is incorrect")
    
    session.close()
    return False, None
