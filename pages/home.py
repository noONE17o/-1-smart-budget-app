import streamlit as st
from database import Session, Transaction
import datetime
import pandas as pd
import matplotlib.pyplot as plt

def show():
    st.title("Home - Smart Budget App")
    st.header("Add a New Transaction")
    
    session = Session()

    with st.form("transaction_form"):
        date = st.date_input("Date", datetime.date.today())
        type = st.selectbox("Type", ["Income", "Expense"])
        category = st.text_input("Category")
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        description = st.text_area("Description")
        submitted = st.form_submit_button("Add Transaction")

        if submitted:
            new_transaction = Transaction(date=date, type=type, category=category, amount=amount, description=description, user_id=1)  # Replace user_id with actual user ID
            session.add(new_transaction)
            session.commit()
            st.success("Transaction added successfully!")

    # Display summary and charts
    transactions = session.query(Transaction).all()
    if transactions:
        df = pd.DataFrame([(t.date, t.type, t.category, t.amount, t.description) for t in transactions],
                          columns=["Date", "Type", "Category", "Amount", "Description"])

        income = df[df['Type'] == 'Income']['Amount'].sum()
        expenses = df[df['Type'] == 'Expense']['Amount'].sum()
        savings = income - expenses
        expense_percentage = (expenses / income) * 100 if income else 0

        st.write(f"Total Income: ${income:.2f}")
        st.write(f"Total Expenses: ${expenses:.2f}")
        st.write(f"Savings: ${savings:.2f} ({expense_percentage:.2f}% of income)")

        st.subheader("Expense Distribution")
        if not df[df['Type'] == 'Expense'].empty:
            expense_distribution = df[df['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
            fig, ax = plt.subplots()
            expense_distribution.plot(kind='bar', ax=ax)
            st.pyplot(fig)

        st.subheader("Transaction History")
        st.dataframe(df)

    # Optional bank transactions feature (simplified for now)
    st.header("Bank Transactions")
    st.write("Feature coming soon...")

    session.close()
