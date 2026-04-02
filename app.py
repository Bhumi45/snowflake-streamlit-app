import streamlit as st
from snowflake.snowpark.context import get_active_session

#create connection
session= get_active_session() #already connected, ready-to-use Snowflake session.
# a snowflake session is a way for a python code to communicate to snowflake.
st.title(" Advisor App")
 # now app is connected to database.

#fetch data
# query = 'SELECT * FROM advisor_db.advisor.client_details'
# data = session.sql(query).to_pandas()

query = 'SELECT client_id,client_name FROM advisor_db.advisor.client_details'
clients = session.sql(query).to_pandas()

# st.write("Client Data")
# st.dataframe(data)

#add dropdown - with this we can select the client whose question/ answer we want to see
selected_client = st.selectbox(" Select Client", clients['CLIENT_NAME'])
st.write("You selected:",selected_client)

# show questions based on client
client_id = clients[clients["CLIENT_NAME"]== selected_client]["CLIENT_ID"].values[0]
# this find client_id of the selected client

query=f"""
SELECT question_id,question_text
FROM advisor_db.advisor.questions
WHERE client_id={client_id}
"""
questions=session.sql(query).to_pandas()
selected_question=st.selectbox("Select Question",questions["QUESTION_TEXT"])

# show answers of the questions asked by selected clients
question_id = questions[questions["QUESTION_TEXT"]==selected_question]["QUESTION_ID"].values[0]

query=f"""
SELECT answer_text 
FROM advisor_db.advisor.answers
WHERE question_id ={question_id}"""

answer = session.sql(query).to_pandas()
st.subheader("Answer")

if not answer.empty:
    st.success(answer["ANSWER_TEXT"].values[0])
else:
    st.warning("No answers found")

