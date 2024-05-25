import os
import json
import traceback
import streamlit as st
from dotenv import load_dotenv
import pandas as pd
from langchain.callbacks import get_openai_callback
import sys
# Add the src directory to the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.append(src_dir)

from MCQ_Gen.utils import read_file , get_table_data
from MCQ_Gen.mcqGenerator import generate_evaluate_chain
from MCQ_Gen.logger import logging

# load response file
with open('RESPONSE.json', "r") as f:
    RESPONSE_JSON = json.load(f)

#create a title for the app
st.title("MCQ generator app with Langchain")

with st.form("user input"):
    uploaded_file = st.file_uploader("Choose a file")
    mcq_count = st.number_input("no. of MCQs", min_value=3, max_value= 50)
    subject = st.text_input("Insert Subject", max_chars=20)
    tone = st.text_input("Complexity level of questions", max_chars=20, placeholder='simple')
    
    button = st.form_submit_button("Create")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text = read_file(uploaded_file)
                
                with get_openai_callback() as cb:      # Count tokens and the cost of API call
                    response=generate_evaluate_chain(
                        {
                            "text": TEXT,
                            "number": NUMBER,
                            "subject":SUBJECT,
                            "tone": TONE,
                            "RESPONSE_JSON": json.dumps(RESPONSE_JSON)
                        }
                        )
                st.write(response)
            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                st.error("Error")

            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
                if isinstance(response, dict):
                    quiz=response.get("quiz", None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        df = pd.Dataframe(table_data)
                        df.index = df.index+1
                        st.table(df)

                        st.text_area(label = 'review', value = response['review']) # Display the review
                    else:
                        st.error("Error in the table data")

                else:
                    st.write(response)
                
                
