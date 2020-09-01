import os
import csv
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

csvpath = os.path.join('Data', 'Skyserver_SQL2_27_2018 6_51_39 PM.csv')
with open(csvpath) as csvfile:
    data = csv.reader(csvfile, delimiter=',')

st.write("""
# Classifying Space Observations as Galaxies, Quasars or Stars
""")

st.sidebar.header('User Input Parameters')


def user_input_features():
    ra = st.sidebar.slider('Right Ascension')
    dec = st.sidebar.slider('Declination')
    u = st.sidebar.slider('U')
    g = st.sidebar.slider('G')
    r = st.sidebar.slider('R')
    i = st.sidebar.slider('I')
    z = st.sidebar.slider('Z')
    redshift = st.sidebar.slider('Redshift')
    data = {'ra': ra,
            'dec': dec,
            'u': u,
            'g': g,
            'r': r,
            'i': i,
            'z': z,
            'redshift': redshift}
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

X = data.data
Y = data.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
# st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
