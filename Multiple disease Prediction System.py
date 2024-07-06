import streamlit as st
from streamlit_option_menu import option_menu
import pickle

# Function to load models
def load_models():
    diabetes_model = pickle.load(open(r'C:/Users/Hp/Desktop/Multiple disease Prediction System/saved/diabetes_model (6).sav', 'rb'))
    heart_disease_model = pickle.load(open(r'C:/Users/Hp/Desktop/Multiple disease Prediction System/saved/heart_disease_model (1).sav', 'rb'))
    return diabetes_model, heart_disease_model

# Function to display diabetes prediction interface
def show_diabetes_interface(diabetes_model):
    st.title('Diabetes Prediction')
    st.write('Enter patient details below:')
    col1, col2 = st.columns(2)
    with col1:
        pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1, key='pregnancies')
        glucose = st.number_input('Glucose Level', min_value=0, key='glucose')
        blood_pressure = st.number_input('Blood Pressure', min_value=0, key='blood_pressure')
        skin_thickness = st.number_input('Skin Thickness', min_value=0, key='skin_thickness')
    with col2:
        insulin = st.number_input('Insulin Level', min_value=0, key='insulin')
        bmi = st.number_input('BMI', min_value=0.0, key='bmi')
        diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0, key='diabetes_pedigree')
        age = st.number_input('Age', min_value=0, key='age')

    if st.button('Predict Diabetes'):
        input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]
        diabetes_prediction = diabetes_model.predict([input_data])
        if diabetes_prediction[0] == 1:
            st.error('The person is predicted to be diabetic.')
        else:
            st.success('The person is predicted not to be diabetic.')

# Function to display heart disease prediction interface
def show_heart_disease_interface(heart_disease_model):
    st.title('Heart Disease Prediction')
    st.write('Enter patient details below:')
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input('Age', min_value=29, max_value=77, key='heart_age')
        sex = st.selectbox('Sex', ['Male(1)', 'Female(0)'], key='heart_sex')
        cp = st.selectbox('Chest Pain Type', ['Typical Angina(0)', 'Atypical Angina(1)', 'Non-anginal Pain(2)', 'Asymptomatic(3)'], key='heart_cp')
        trestbps = st.number_input('Resting Blood Pressure', min_value=94, max_value=200, key='heart_trestbps')
        chol = st.number_input('Cholesterol', min_value=126, max_value=564, key='heart_chol')
        fbs = st.selectbox('Fasting Blood Sugar', ['> 120 mg/dl(1)', '<= 120 mg/dl(0)'], key='heart_fbs')
    with col2:
        restecg = st.selectbox('Resting ECG', ['Normal(0)', 'ST-T wave abnormality(1)', 'Left ventricular hypertrophy(2)'], key='heart_restecg')
        thalach = st.number_input('Max Heart Rate', min_value=71, max_value=202, key='heart_thalach')
        exang = st.selectbox('Exercise Induced Angina', ['Yes(1)', 'No(0)'], key='heart_exang')
        oldpeak = st.number_input('ST Depression', min_value=0.0, max_value=6.2, key='heart_oldpeak')
        slope = st.selectbox('Slope of ST Segment', ['Upsloping(0)', 'Flat(1)', 'Downsloping(2)'], key='heart_slope')
        ca = st.number_input('Number of Major Vessels', min_value=0, max_value=3, key='heart_ca')
        thal = st.selectbox('Thalassemia', ['Normal(0)', 'Fixed Defect(1)', 'Reversible Defect(2)'], key='heart_thal')

    if st.button('Predict Heart Disease'):
        sex_value = 1 if sex == 'Male(1)' else 0
        cp_value = ['Typical Angina(0)', 'Atypical Angina(1)', 'Non-anginal Pain(2)', 'Asymptomatic(3)'].index(cp)
        fbs_value = 1 if fbs == '> 120 mg/dl(1)' else 0
        restecg_value = ['Normal(0)', 'ST-T wave abnormality(1)', 'Left ventricular hypertrophy(2)'].index(restecg)
        exang_value = 1 if exang == 'Yes(1)' else 0
        slope_value = ['Upsloping(0)', 'Flat(1)', 'Downsloping(2)'].index(slope)
        thal_value = ['Normal(0)', 'Fixed Defect(1)', 'Reversible Defect(2)'].index(thal)

        heart_input_data = [age, sex_value, cp_value, trestbps, chol, fbs_value, restecg_value, thalach, exang_value, oldpeak, slope_value, ca, thal_value]
        heart_prediction = heart_disease_model.predict([heart_input_data])
        if heart_prediction[0] == 1:
            st.error('The person is predicted to have heart disease.')
        else:
            st.success('The person is predicted not to have heart disease.')

# Set page configuration
st.set_page_config(
    page_title="Health Assistant",
    layout="wide",
    page_icon="🧑‍⚕️"
)

# Load models
diabetes_model, heart_disease_model = load_models()

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction'],
        menu_icon='🏥',
        icons=['🩺', '❤️'],
        default_index=0
    )
    
# Display selected page with hospital background image
if selected == 'Diabetes Prediction':
    # Insert hospital background image
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background: url('C:/Users/Hp/Desktop/Multiple disease Prediction System/diabetes_pic');
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    show_diabetes_interface(diabetes_model)
elif selected == 'Heart Disease Prediction':
    # Insert hospital background image
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background: url('C:/Users/Hp/Desktop/Multiple disease Prediction System/heart_pic');
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    show_heart_disease_interface(heart_disease_model)



