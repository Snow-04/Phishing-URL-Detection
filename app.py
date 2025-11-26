import streamlit as st
import pandas as pd
import pickle
from extract_features import extract_features

st.title("Phishing URL Detector (RF + ANN)")

model_rf = pickle.load(open("model_rf.pkl","rb"))
model_ann = pickle.load(open("model_ann.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))
selected_features = pickle.load(open("features.pkl","rb"))

url = st.text_input("Enter a URL:")

if st.button("Predict"):
    f = extract_features(url)
    input_df = pd.DataFrame([f])[selected_features]

    rf_pred = model_rf.predict(input_df)[0]
    ann_pred = model_ann.predict(scaler.transform(input_df))[0]

    st.subheader("Random Forest:")
    st.write(rf_pred)

    st.subheader("ANN:")
    #st.write("phishing" if ann_pred==1 else "legitimate")
    st.write(ann_pred)
