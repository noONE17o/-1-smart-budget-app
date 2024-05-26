import streamlit as st
from database import Session, Goal

def show():
    st.title("Financial Goals")
    
    session = Session()

    with st.form("goal_form"):
        goal_name = st.text_input("Goal Name")
        amount_needed = st.number_input("Amount Needed", min_value=0.0, format="%.2f")
        priority = st.slider("Priority", min_value=1, max_value=5)
        savings_percentage = st.slider("Savings Percentage", min_value=0.0, max_value=100.0, format="%.1f")
        submitted = st.form_submit_button("Add Goal")

        if submitted:
            new_goal = Goal(goal_name=goal_name, amount_needed=amount_needed, priority=priority, savings_percentage=savings_percentage)
            session.add(new_goal)
            session.commit()
            st.success("Goal added successfully!")

    st.header("Your Goals")
    goals = session.query(Goal).all()
    for goal in goals:
        st.write(f"Goal: {goal.goal_name}, Amount Needed: ${goal.amount_needed:.2f}, Priority: {goal.priority}, Savings Percentage: {goal.savings_percentage}%")

    session.close()
