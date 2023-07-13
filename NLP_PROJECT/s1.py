import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
data = pd.read_csv('drug_sl.csv')
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(data['condition'])
y_train = data['drugName']
naive_bayes_model = MultinomialNB()
naive_bayes_model.fit(X_train, y_train)
st.title("Top Drugs Predictor")
conditions = data['condition'].unique()
condition = st.selectbox("Select a condition", options=[None] + list(conditions), index=0)

if condition:
    # Predict the top drugs for the selected condition
    X_condition = vectorizer.transform([condition])
    drug_probabilities = naive_bayes_model.predict_proba(X_condition)[0]
    top_drug_indices = drug_probabilities.argsort()[::-1][:5]
    top_drugs = list(set([naive_bayes_model.classes_[index] for index in top_drug_indices]))

    # Display the top drugs
    st.write(f"Top Drugs for '{condition}':")
    for drug in top_drugs:
        st.write(drug)
