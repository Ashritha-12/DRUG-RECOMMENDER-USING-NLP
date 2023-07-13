import pandas as pd
import streamlit as st

# Load the dataset
data = pd.read_csv('drug_sl.csv')  # Replace 'drug_sl.csv' with the path to your dataset

# Calculate the mean score per condition
mean_scores = data.groupby('condition')['overall_score'].mean().reset_index()

# Sort the mean scores in descending order
mean_scores = mean_scores.sort_values(by='overall_score', ascending=False)


# Create a function to display the top drugs for a given condition
def display_top_drugs(condition):
    top_drugs = data[data['condition'] == condition]
    unique_drugs = top_drugs['drugName'].unique()
    top_5_drugs = unique_drugs[:5]
    for drug in top_5_drugs:
        st.write(drug)

# Get the unique conditions in the dataset
conditions = data['condition'].unique()

# Create a Streamlit app
def main():
    st.title('Top Drugs by Condition')
    
    # Create a dropdown menu to select the condition
    condition = st.selectbox('Select a condition', options=[None] + list(conditions), index=0)
    
    # Display the top drugs for the selected condition
    if condition is not None:
        display_top_drugs(condition)

if __name__ == '__main__':
    main()
