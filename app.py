from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as generativeai

## Configure our API key 
generativeai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## Function to load google Gemini model and provide sql query as response
def get_genimi_response(question,prompt):
    model =generativeai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

## Function to retrieve query from sql data base

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(rows)
    return rows

## Define your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query! 
    The SQL database has two tables \nThe table 1 STUDENT and has the following columns - NAME, CLASS, 
    SECTION and MARKS and another table 2 PROFILE and has the following columns - NAME, SEX AND REGION
    \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science";
    \n\nFor example,\nExample 3 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM PROFILE ;
    \nExample 4 - Tell me all the students from Pune?, 
    the SQL command will be something like this SELECT * FROM PROFILE 
    where REGION="Pune"; 
    \nExample 5 - Give me name,marks,section,class and are from Pune?, 
    the SQL command will be something like this SELECT NAME,MARKS,SECTION,CLASS,REGION FROM PROFILE INNER JOIN STUDENT ON PROFILE.NAME = STUDENT.NAME where REGION="Pune"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """

]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is pressed
if submit:
    response = get_genimi_response(question,prompt)
    print(response)
    data = read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)
    print(data)









