import streamlit as st
from pathlib import Path
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

st.set_page_config(page_title="Chat SQL", page_icon=":parrot:")
st.title("Langchain: Chat with SQL DB")

LOCAL_DB = "USE_LOCAL_DB"
MYSQL="USE_MYSQL"

radio_opt=["use SQLite3 Database - Student.db", "Connect to your MySQL DB"]

selected_option = st.sidebar.radio(label="Choose the db with which you want to chat", options=radio_opt)

if radio_opt.index(selected_option) == 1:
    db_uri=MYSQL
    mysql_host = st.sidebar.text_input("provide my SQL Host")
    mysql_user = st.sidebar.text_input("MYSQL User")
    mysql_password = st.sidebar.text_input("MYSQL Password", type="password")
    mysql_db = st.sidebar.text_input("MYSQL Database Name")
else:
    db_uri = LOCAL_DB

api_key = st.sidebar.text_input(label="Enter Groq API Key", type="password")

if not db_uri:
    st.info("Please select a database to proceed.")

if not api_key:
    st.info("Please enter your Groq API Key to proceed.")

#LLM model
llm = ChatGroq(groq_api_key=api_key, model="qwen/qwen3-32b", streaming=True)

def configure_db(db_uri, mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None):
    if db_uri == LOCAL_DB:
        db_filepath = (Path(__file__).parent/"student.db").absolute()
        print(db_filepath)
        creator = lambda: sqlite3.connect(f"file:{db_filepath}?mode=ro", uri=True)
        return SQLDatabase(create_engine("sqlite:///", creator=creator))
    elif db_uri == MYSQL:
        if not all([mysql_host, mysql_user, mysql_password, mysql_db]):
            st.error("Please provide all MySQL connection details.")
            st.stop()
        engine = create_engine(f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}")
        return SQLDatabase.from_uri(engine.url)
    
if db_uri==MYSQL:
    db = configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_db)
else:
    db = configure_db(db_uri)

#toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I am your SQL assistant. How can I help you today?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_query=st.chat_input(placeholder="Ask a question about the database")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)
    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(
            {"input": user_query},
            callbacks=[streamlit_callback]
        )
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)