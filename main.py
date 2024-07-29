from langchain_helper_file import get_chain
import streamlit as st
import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
st.title("Retail T-Shirt Store Database : Q&A Agent")

# Tabs for Q&A and Database
tab1, tab2 = st.tabs(["Q&A Agent", "Database Information"])

with tab1:
    question = st.text_input("Question : ")

    if question:
        chain = get_chain()
        ans = chain.invoke(question)
        st.header("Answer : ")
        st.write(ans['result'])

with tab2:
    st.header("Database Information")

    # Database connection details
    db_user = os.environ["USER"]
    db_password = os.environ["PASSWORD"]
    db_host = os.environ["HOST"]
    db_name = os.environ["DATABASE"]

    # Connect to the database
    cnx = mysql.connector.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        database=db_name,
        auth_plugin='mysql_native_password'  # Ensure the correct authentication plugin
    )

    # Query and display t_shirts table
    st.subheader("t_shirts Table")
    query_tshirts = "SELECT * FROM t_shirts"
    df_tshirts = pd.read_sql(query_tshirts, cnx)
    st.write(df_tshirts)

    # Query and display discounts table
    st.subheader("discounts Table")
    query_discounts = "SELECT * FROM discounts"
    df_discounts = pd.read_sql(query_discounts, cnx)
    st.write(df_discounts)


    # Close the connection
    cnx.close()
