import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import base64

# Function to load models
def load_models():
    diabetes_model = pickle.load(open(r'C:/Users/Hp/Desktop/Multiple disease Prediction System/saved/diabetes_model (6).sav', 'rb'))
    heart_disease_model = pickle.load(open(r'C:/Users/Hp/Desktop/Multiple disease Prediction System/saved/heart_disease_model (1).sav', 'rb'))
    return diabetes_model, heart_disease_model

# Function to set background image
def set_background(image_file):
    """
    Sets the background image for the Streamlit app.
    
    Parameters:
    image_file (str): Path to the background image file.
    """
    with open(image_file, "rb") as file:
        base64_string = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{base64_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to display custom styled messages
def custom_message(message, message_type):
    """
    Displays a custom styled message in Streamlit.

    Parameters:
    message (str): The message to display.
    message_type (str): The type of message ('error' or 'success').
    """
    if message_type == 'error':
        st.markdown(
            f"<p style='color: red; font-size: 50px; font-weight: bold;'>{message}</p>", 
            unsafe_allow_html=True
        )
    elif message_type == 'success':
        st.markdown(
            f"<p style='color: green; font-size: 50px; font-weight: bold;'>{message}</p>", 
            unsafe_allow_html=True
        )

# Set page configuration
st.set_page_config(
    page_title="Health Assistant",
    layout="wide",
    page_icon="🧑‍⚕️",
    initial_sidebar_state="expanded"
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
        default_index=0,
        styles={
            "nav-link-selected": {"background-color": "#1f77b4"}
        }
    )

# Function to create bold white text using st.markdown
def bold_white_text(label):
    return st.markdown(f"<span style='color:white; font-weight:bold;'>{label}</span>", unsafe_allow_html=True)

# Set the background image according to the selected option
if selected == 'Diabetes Prediction':
    set_background('C:/Users/Hp/Desktop/Multiple disease Prediction System/diabetes_pic.jpg')
    st.title('Diabetes Prediction')
    st.write('Enter patient details below:')
    col1, col2 = st.columns(2)
    with col1:
        bold_white_text("Number of Pregnancies")
        pregnancies = st.number_input('', min_value=0, max_value=17, key='pregnancies', help="Enter the number of times the patient has been pregnant.")
        bold_white_text("Glucose Level")
        glucose = st.number_input('', min_value=0,max_value=199, key='glucose', help="Enter the patient's glucose level in mg/dL.")
        bold_white_text("Blood Pressure")
        blood_pressure = st.number_input('', min_value=0, max_value=122, key='blood_pressure', help="Enter the patient's blood pressure in mm Hg.")
        bold_white_text("Skin Thickness")
        skin_thickness = st.number_input('', min_value=0, max_value=99, key='skin_thickness', help="Enter the skin thickness in mm.")
    with col2:
        bold_white_text("Insulin Level")
        insulin = st.number_input('', min_value=0, max_value=846,key='insulin', help="Enter the patient's insulin level in μU/mL.")
        bold_white_text("BMI")
        bmi = st.number_input('', min_value=0.0,max_value=67.1, key='bmi', help="Enter the patient's Body Mass Index.")
        bold_white_text("Diabetes Pedigree Function")
        diabetes_pedigree = st.number_input('', min_value=0.08,max_value=2.42, key='diabetes_pedigree', help="Enter the diabetes pedigree function.")
        bold_white_text("Age")
        age = st.number_input('', min_value=21,max_value=81, key='age', help="Enter the patient's age.")
    
    if st.button('Predict Diabetes'):
        input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]
        with st.spinner('Predicting...'):
            diabetes_prediction = diabetes_model.predict([input_data])
        if diabetes_prediction[0] == 1:
            custom_message('The person is predicted to be diabetic.', 'error')
        else:
            custom_message('The person is predicted not to be diabetic.', 'success')

elif selected == 'Heart Disease Prediction':
    set_background('C:/Users/Hp/Desktop/Multiple disease Prediction System/heart_pic.jpg')
    st.title('Heart Disease Prediction')
    st.write('Enter patient details below:')
    col1, col2 = st.columns(2)
    with col1:
        bold_white_text("Age")
        age = st.number_input('', min_value=29, max_value=77, key='heart_age', help="Enter the patient's age.")
        bold_white_text("Sex")
        sex = st.selectbox('', ['Male(1)', 'Female(0)'], key='heart_sex', help="Select the patient's sex.")
        bold_white_text("Chest Pain Type")
        cp = st.selectbox('', ['Typical Angina(0)', 'Atypical Angina(1)', 'Non-anginal Pain(2)', 'Asymptomatic(3)'], key='heart_cp', help="Select the type of chest pain experienced.")
        bold_white_text("Resting Blood Pressure")
        trestbps = st.number_input('', min_value=94, max_value=200, key='heart_trestbps', help="Enter the patient's resting blood pressure in mm Hg.")
        bold_white_text("Cholesterol")
        chol = st.number_input('', min_value=126, max_value=564, key='heart_chol', help="Enter the patient's cholesterol level in mg/dL.")
        bold_white_text("Fasting Blood Sugar")
        fbs = st.selectbox('', ['> 120 mg/dl(1)', '<= 120 mg/dl(0)'], key='heart_fbs', help="Select the patient's fasting blood sugar level.")
    with col2:
        bold_white_text("Resting ECG")
        restecg = st.selectbox('', ['Normal(0)', 'ST-T wave abnormality(1)', 'Left ventricular hypertrophy(2)'], key='heart_restecg', help="Select the result of the patient's resting ECG.")
        bold_white_text("Max Heart Rate")
        thalach = st.number_input('', min_value=71, max_value=202, key='heart_thalach', help="Enter the patient's maximum heart rate achieved.")
        bold_white_text("Exercise Induced Angina")
        exang = st.selectbox('', ['Yes(1)', 'No(0)'], key='heart_exang', help="Select if the patient has exercise-induced angina.")
        bold_white_text("ST Depression")
        oldpeak = st.number_input('', min_value=0.0, max_value=6.2, key='heart_oldpeak', help="Enter the ST depression induced by exercise relative to rest.")
        bold_white_text("Slope of ST Segment")
        slope = st.selectbox('', ['Upsloping(0)', 'Flat(1)', 'Downsloping(2)'], key='heart_slope', help="Select the slope of the peak exercise ST segment.")
        bold_white_text("Number of Major Vessels")
        ca = st.number_input('', min_value=0, max_value=3, key='heart_ca', help="Enter the number of major vessels colored by fluoroscopy.")
        bold_white_text("Thalassemia")
        thal = st.selectbox('', ['Normal(0)', 'Fixed Defect(1)', 'Reversible Defect(2)'], key='heart_thal', help="Select the patient's thalassemia status.")
    
    if st.button('Predict Heart Disease'):
        sex_value = 1 if sex == 'Male(1)' else 0
        cp_value = ['Typical Angina(0)', 'Atypical Angina(1)', 'Non-anginal Pain(2)', 'Asymptomatic(3)'].index(cp)
        fbs_value = 1 if fbs == '> 120 mg/dl(1)' else 0
        restecg_value = ['Normal(0)', 'ST-T wave abnormality(1)', 'Left ventricular hypertrophy(2)'].index(restecg)
        exang_value = 1 if exang == 'Yes(1)' else 0
        slope_value = ['Upsloping(0)', 'Flat(1)', 'Downsloping(2)'].index(slope)
        thal_value = ['Normal(0)', 'Fixed Defect(1)', 'Reversible Defect(2)'].index(thal)
        
        heart_input_data = [age, sex_value, cp_value, trestbps, chol, fbs_value, restecg_value, thalach, exang_value, oldpeak, slope_value, ca, thal_value]
        with st.spinner('Predicting...'):
            heart_prediction = heart_disease_model.predict([heart_input_data])
        if heart_prediction[0] == 1:
            custom_message('The person is predicted to have heart disease.', 'error')
        else:
            custom_message('The person is predicted not to have heart disease.', 'success')



