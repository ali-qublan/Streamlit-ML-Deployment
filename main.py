import numpy as np
import streamlit as st

import pickle


model = pickle.load(open('model.pkl','rb'))


def wellcome():
    return "Wellcome Ali"


def predict_note_authentication(R_D,Administartion,Marketing):
    
    prediction=model.predict([[R_D,Administartion,Marketing]])
    print(prediction)
    return prediction

def main():
    st.title("Profit Prediction")
    html_temp = """
    <div style="background-color:RebeccaPurple;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Profit Predictin ML </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    R_D = st.text_input("R&D","Type Here")
    Administartion = st.text_input("Administartion","Type Here")
    Marketing = st.text_input("Marketing","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(R_D,Administartion,Marketing)
    st.success('The output is {}'.format(result))



if __name__=='__main__':
    main()