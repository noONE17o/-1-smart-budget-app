import streamlit as st
from auth import login
import pages.home as home
import pages.goals as goals
import pages.chatbot as chatbot
import pages.news as news
import pages.settings as settings
import pages.register as register

st.set_page_config(page_title="Smart Budget App", layout="wide")

menu = ["Login", "Register"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Login":
    authenticated, name = login()

    if authenticated:
        st.sidebar.title(f"Welcome, {name}")
        st.sidebar.title("Navigation")
        pages = {
            "1. Home": home,
            "2. Financial Goals": goals,
            "3. Chatbot": chatbot,
            "4. News & Currency": news,
            "5. Settings": settings
        }
        
        page_selection = st.sidebar.radio("Go to", list(pages.keys()))
        selected_page = pages[page_selection]
        selected_page.show()
    else:
        st.write("Please log in to access the Smart Budget App.")
elif choice == "Register":
    register.show()
