import streamlit as st
import pickle
import numpy as np 


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
         data = pickle.load(file)
    return data 


data = load_model()

regressor = data['model']
le_employee_residence = data['le_employee_residence']
le_experience_level = data['le_experience_level']

def show_predict_page():
    st.title('DATA SCIENCE SALARY PREDICTION')
    st.write('''### some information is needed to predict salary''')

    employee_residence = (
      'US',       
      'GB',        
      'CA',             
      'ES',         
      'DE',          
      'IN',          
      'FR',          
      'AU',         
      'PT',          
      'NL',          
      'BR',          
      'IT',          
      'GR',         
      'CO',          
      'LT',          
      'ZA',
    )

    experience_level = (
      'EN',
      'MI',
      'EX',
      'SE',
    )

    employee_residence = st.selectbox('employee_residence', employee_residence)
    experience = st.selectbox('experience_level', experience_level)
    Yes = st.button('predict salary')
    if Yes:
        x = np.array([[employee_residence, experience]])
        x[:,0] = le_employee_residence.transform(x[:,0])
        x[:,1] = le_experience_level.transform(x[:,1])
        x = x.astype(float)

        salary = regressor.predict(x)
        st.subheader(f"The predicted salary is ${salary[0]:.2f}")


