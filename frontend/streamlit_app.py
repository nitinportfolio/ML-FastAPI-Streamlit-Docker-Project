# In order to access frontend web app, Run "st app streamlit_app.py"

import streamlit as st
# requests to send http request
import requests
import json


def run():
    st.title("Campus Placement Classifier")
    sl_no = st.text_input("Serial Number")
    ssc_p = st.text_input("SSC (10th) Percentage")
    hsc_p = st.text_input("HSC (12th) percentage")
    degree_p = st.text_input("Degree Percentage")
    etest_p = st.text_input("employability test percentage (conducted by the college)")
    mba_p = st.text_input("MBA percentage")
    gender = st.selectbox("Gender", ['Male', 'Female'])
    ssc_b = st.selectbox("SSC Board of Education", ['Central', 'Others'])
    hsc_b = st.selectbox("HSC Board of Education", ['Central', 'Others'])
    hsc_s = st.selectbox("Specialization in HSC", ['Commerce', 'Science', 'Arts'])
    degree_t = st.selectbox("Under Graduation (Degree type)", ['Sci&Tech', 'Comm&Mgmt'])
    workex = st.selectbox("Work Experience", ['Yes', 'No'])
    specialisation = st.selectbox("Post Graduation(MBA)- Specialization", ['Mkt&HR', 'Mkt&Fin'])

    data = {
        'sl_no': sl_no,
        'ssc_p': ssc_p,
        'hsc_p': hsc_p,
        'degree_p': degree_p,
        'etest_p': etest_p,
        'mba_p': mba_p,
        'gender': gender,
        'ssc_b': ssc_b,
        'hsc_b': hsc_b,
        'hsc_s': hsc_s,
        'degree_t': degree_t,
        'workex': workex,
        'specialisation': specialisation
        }

    if st.button("Predict"):
        # post request to ML FastAPI running at below address & will pass json data from streamlit user above
        response = requests.post("http://127.0.0.1:8000/predict",json=data)
        prediction = response.text
        st.success(f"The prediction from model: {prediction}")

if __name__ == "__main__":
    # By default, it will run at 8501 port
    run()