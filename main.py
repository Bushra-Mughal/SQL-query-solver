##Dependancies:
from sqlalchemy import create_engine , text     #--->  acts as a bridge between python and Database.It executes query on MySql and fetchs results to python 
import pymysql                                  #--> to easily connect to local MySql server
import streamlit                                #---> a python web framework library (easier than flask , fast )

import subprocess                               #--->  to execute "ollama pull deepseek-r1:1.5b" automatically
import requests                                 #--->to send HTTP requests to the Ollama API , running locally.

import pandas as pd                             #---> for loading Relational Database table
import re                                       #---> helps you search for patterns in text

##Ollama DEFAULT ENDPOINT:
OLLAMA_API_URL = "http://localhost:11434/api/generate"  #--->You talk to OLLAMA using a URL because it acts like a mini-website (API server) 

##RUN THIS LINE TO ACTIVATE LOCAL AI:   (for nerds: pull local llm using Ollama)
# subprocess.run(["ollama", "pull", "deepseek-r1:1.5b"])

##RUN THIS QUERY ON MYSQL DATABASE:    (for nerds: inorder to avoid 'cryptography' package )
#  ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_mysql_password_here';
#  FLUSH PRIVILEGES;


def chat_with_deepseek(prompt):
    try:
        data = {
            "model": "deepseek-r1:1.5b",   # Your installed model name
            "prompt": prompt,
            "stream": False                # Disable streaming for simplicity
        }
        response = requests.post(OLLAMA_API_URL, json = data)
        response.raise_for_status()        # Check for HTTP errors
        return response.json()["response"]
    except Exception as e:
        return f"Error: {str(e)}"


def extract_sql(text):
    import re
    # 1. Remove <think>...</think>
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)

    # 2. Match first capitalized SQL query (with or without ;)
    match = re.search(r"\b(SELECT|INSERT|UPDATE|DELETE|CREATE|DROP|ALTER)[^;]*;?", text, flags=re.DOTALL)
    if match:
        sql = match.group(0).strip()
        # Ensure it ends with semicolon
        if not sql.endswith(";"):
            sql += ";"
        return sql
    return None   


def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Chatbot: Goodbye!")
            return -1
        
        elif user_input.lower() in ["search"]:
            response = chat_with_deepseek(user_input)
            print("Chatbot: ",response)
            return -1
        
        else:
            response = chat_with_deepseek(
            f"Write ONLY a correct MySQL 8.0 SQL query for table emp (columns: empno, ename, job, mgr, hiredate, sal, comm, deptno). "
            f"No explanation, no extra text.Query must must end with a semicolon and have no alliances and no 'END'. "
            f"User request: {user_input}"
            )
            ##Extract SQL query from the AI's response:
            query = extract_sql(response)
            print("SQL query :", query , end="\n\n" )
            print("Answer: ")
            return query
        
def main():
    ## Using CORE method for executing queries:
    # engine = create_engine("mysql+pymysql://root:yourpassword@localhost:3306/mydatabase")
    engine = create_engine("mysql+pymysql://root:DesignProdigyismymysql%40@localhost:3306/mam_sana")
        # root → your MySQL username
        # yourpassword → your MySQL password (use URL encodings if password includes special characters. ie: '%40' for '@')
        # localhost → your server (or IP if remote)
        # mydatabase → your database name
    with engine.connect() as conn:  
        emp = pd.read_sql("SELECT * FROM emp", conn)          #loading the table 

    print("Hey! I am your personal MySql query solver , how may I help you today?")
    while True:
        try:
            query = chat()
            if query== -1:
                break
            else:
                with engine.connect() as conn:
                    result = conn.execute(text(query))
                    for row in result:
                        print(row)
                print("\n\n")

        except:
            print("Error occcured......")
            continue

        user = input("Want to exit? (y / n)")
        if user.lower()=='y':
            print('Good bye!')
            break

if __name__=='__main__':
    main()