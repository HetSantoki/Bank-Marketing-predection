'''
author : santoki het
github : @SantokiHet
organization : L.J University
'''
import os
import sys
import streamlit as st
from evalaute import *

# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

   
class Main:
    def __init__(self) -> None:
        pass

    def run(self):
        
        st.write()
        st.write()
        
        t = TestData()
        t.testing()

        st.markdown("[GitHub](https://github.com/SantokiHet/Bank-Marketing-Campaign.git) | <a href='https://www.linkedin.com/in/het-santoki-9180a2291' target='_blank'>Linkedin</a>",unsafe_allow_html=True)
        
        # Add a LinkedIn profile hyperlink using HTML
        st.markdown("", unsafe_allow_html=True)

        # Add copyright notice at the bottom
        st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line to separate content
        st.markdown(
            "<b><p style='text-align: center; font-size: 12px;'>&copy; 2024 Karan Chauhan. All Rights Reserved.</p>", 
            unsafe_allow_html=True
        )
        
if  __name__ == "__main__":    
    st.markdown("<h1 style='text-align: center;'><b>Bank Marketing Campaign</b></h1>", unsafe_allow_html=True)

    st.markdown("<p ><b> - About this project  :</b></p>",unsafe_allow_html=True)
    st.write(" - This project uses a dataset collected from a bank's marketing campaign. The goal is to develop a neural network model to predict whether a customer will subscribe to a term deposit or not, based on various customer attributes and past campaign details.")

    run_obj = Main()
    run_obj.run()

else  : 
    print("This is a Streamlit app. Please run it using `streamlit run app.py `")  # noqa: E501