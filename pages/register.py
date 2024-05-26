import streamlit as st
from database import Session, User
import bcrypt

def show():
    st.title("Register")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if password != confirm_password:
            st.error("Passwords do not match")
            return

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        session = Session()
        user = User(username=username, email=email, hashed_password=hashed_password)

        try:
            session.add(user)
            session.commit()
            st.success("User registered successfully")
        except Exception as e:
            session.rollback()
            st.error(f"Error: {e}")
        finally:
            session.close()
