import streamlit as st

st.title("Welcome to flameboy ") 
st.header("Python")
st.subheader("Java")
st.markdown("I love python")
st.code("""for i in range(1,5,1):
            print("Hello")
        
        """)

import pandas as pd 
dataset = pd.read_csv("Advertising.csv")
st.dataframe(dataset)

name = st.text_input("Enter your name : ")
fname= st.text_input("Enter your father's name")
mname= st.text_input("Enter your mother's name")
adr= st.text_area("Enter your Text: ")
classdata= st.selectbox("Enter your Class: ",(1,2,3,4,5,6))



button = st.button("Done")
if button:
    # st.write("button pressed")
    # st.write(f"Debug: {name}, {fname}, {mname}, {adr}, {classdata}")
    # st.markdown(f"""
    # Name :{name}           
    # Father Name :{fname}
    # Mother Name :{mname}
    # Address:{adr}
    # Class :{classdata}""") 
    st.write("Button was pressed")
    st.write(f"Name: {name}")
    st.write(f"Father Name: {fname}")
    st.write(f"Mother Name: {mname}")
    st.write(f"Address: {adr}")
    st.write(f"Class: {classdata}")

