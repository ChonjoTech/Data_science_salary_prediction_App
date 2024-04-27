import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i]>= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'other'
    return categorical_map 

st.cache_data
def load_data():
    data = pd.read_csv('DataScience_salaries_2024.csv')
    data = data[['employee_residence' , 'experience_level', 'employment_type', 'salary_in_usd']]
    data = data.dropna()
    data = data[data['employment_type'] == 'FT']
    data = data.drop('employment_type', axis = 1)
    employee_residence_map = shorten_categories(data.employee_residence.value_counts(), 15)
    data['employee_residence' ] = data['employee_residence'].map(employee_residence_map)
    data = data[data['salary_in_usd'] <= 250000]
    data = data[data['salary_in_usd'] >= 5000]
    data = data[data['employee_residence'] != 'other']
    return data 

data = load_data()

def show_explore_page():
    st.title('EXPLORE DATA SCIENCE SALARIES')


    df= data['employee_residence'].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(df, labels = df.index,autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')

    st.write('''#### Data from different countries.''')
    st.pyplot(fig1)

    st.write(
        '''
        ### Average Salary Based on Employee Residence
        '''
    )

    df = data.groupby(['employee_residence'])['salary_in_usd'].mean().sort_values(ascending=True)
    st.bar_chart(df)

    