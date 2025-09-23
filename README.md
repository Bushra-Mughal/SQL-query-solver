<html>
    <h1><U>SQL query solver</U></h1>
    <h4><i>Your personal SQL bot</i></h4>
    <h3>Intro:</h3>
    <p>
        'SQL query solver' is a fully localized python-backend system which efficiently executes RDB (relational database) queries ie: What is the maximum salary? 
        and fetches query results from your local MySQL server.
    </p>
    <h3>Problem considered:</h3>
    <p>
        Storing big data into databases,generaly Relational databases (MySQL) is an efficient and common approach but, to execute a 'SQL query' , inorder to fetch meaningful information , is a
        challenging task for non-technical person ,therefore I developed 'SQL query solver' which enables the user to enter a query in Natural Language (ie: what is the name of highest paying employee?)
        and fetches the result from user's local database. In simple words , NO MORE "SELECT * FROM emp WHERE sal IN(SELECT MAX(sal) FROM dept WHERE....).." 😊🚀

        The best part is this setup is fully localalized (offline) which implies that your data is fully secured from unauthorized access or malware attacks, which is a plus for low-cost organizations or startups.
    </p>
    <h3>Technical stack:</h3>
    <p>
        ◾python streamlit --- for web-UI
        ◾Space efficient local LLM: deepseek-r1:1.5b via Ollama version is 0.5.13
        ◾sqlalchemy and pymysql --- for MySQL database connectivity
        ◾python requests --- for conversation with local LLM
    </p>
    <h3>Workflow in simple steps:</h3>
    <p>
        After connecting to MySQL server: 
        1. User enters the question in Natural Language on the UI
        2. Local LLM (in this case: deepseek r1) converts the question into an executable SQL query
        3. SQL query is executed on MySQL server 
        4. Result is fetched and displayed back to the user
    </p>
    <h3>Modifications as per requirement:</h3>
    <p>
        ◾It is suggested to integrate a local LLM having more parameterized functions (ie: >1.5 billion parameters), to ensure efficiency in complex SQL queries and less errors.
    </p>
    <h3>Steps for installation:</h3>
    <p>


        1. Install python dependancies:  (~200 MB)

        CMD:  pip install streamlit pandas pymysql sqlalchemy requests

        2. Install Ollama:
        
        Download from: https://ollama.ai/download
        Run the .exe installer
        
        3. Download AI model:
        
        CMD: ollama pull deepseek-r1:1.5b

        4. Set up MySQL:

        Open MySQL Workbench
        Run:
        SQL:  ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password';
              FLUSH PRIVILEGES;
        
        5. Clone github repo:
        Copy-paste the code file to local drive
        CMD: streamlit run app.py
    </p>
</html>