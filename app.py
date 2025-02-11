import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide', 
                   page_icon='👩🏻‍⚕️')

diabetes_model = pickle.load(open(r"C:\Users\Lenovo\Desktop\Disease Outbreak\models\diabetes_model.sav",'rb'))

heart_model = pickle.load(open(r"C:\Users\Lenovo\Desktop\Disease Outbreak\models\heart_model.sav",'rb'))

parkinsons_model = pickle.load(open(r"C:\Users\Lenovo\Desktop\Disease Outbreak\models\parkinsons_model.sav",'rb'))


with st.sidebar:
    selected=option_menu('Prediction of Diesease Outbreak System',
                         ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                         menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prection Using Ml')
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
        Glucose=st.text_input('Glucose Level')
    with col3:
        Blood_Pressure=st.text_input('Blood Pressure')
    with col1:
        SkinThickness=st.text_input('Skin Thickness')
    with col2:
        Insulin=st.text_input('Insulin Level')
    with col3:
        BMI=st.text_input('BMI')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function')
    with col2:
        Age=st.text_input('Age')

    diab_diagnosis=''

    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies,Glucose,Blood_Pressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input=[float(x) for x in user_input]
        diab_prediction=diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis='The person is diabetic'
        else:
            diab_diagnosis='The person is not diabetic'
    st.success(diab_diagnosis)


if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction Using Ml')
    col1,col2,col3,col4=st.columns(4)
    with col1:
        Age=st.text_input('Age')
    with col2:
        Sex=st.text_input('Sex')
    with col3:
        ChestPainType=st.text_input('Chest Pain Type')
    with col4:
        RestingBloodPressure=st.text_input('Resting Blood Pressure')
    with col1:
        CholesterolLevel=st.text_input('Cholesterol Level')
    with col2:
        FastingBloodSugar=st.text_input('Fasting Blood Sugar')
    with col3:
        RestingECGResults=st.text_input('Resting ECG Results')
    with col4:
        MaximumHeartRate=st.text_input('Maximum Heart Rate')
    with col1:
        ExerciseInducedAngina=st.text_input('Exercise Induced Angina')
    with col2:
        STDepressionInducedbyExercise=st.text_input('ST Depression Induced by Exercise')
    with col3:
        SlopeoftheSTSegment=st.text_input('Slope of the ST Segment')
    with col4:
        NumberofMajorVessels=st.text_input('Number of Major Vessels (Fluoroscopy)')
    with col1:
        ThalassemiaType=st.text_input('Thalassemia Type')
    
    heart_diagnosis=''

    if st.button('Heart Disease Test Result'):
        user_input=[Age,Sex,ChestPainType,RestingBloodPressure,CholesterolLevel,FastingBloodSugar,RestingECGResults,MaximumHeartRate,
                    ExerciseInducedAngina,STDepressionInducedbyExercise,SlopeoftheSTSegment,NumberofMajorVessels,ThalassemiaType]
        user_input=[float(x) for x in user_input]
        heart_prediction=heart_model.predict([user_input])
        if heart_prediction[0]==1:
            heart_diagnosis='The person suffers with heart disease.'
        else:
            heart_diagnosis='The person is not suffering with any heart disease.'
    st.success(heart_diagnosis)

if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction Using Ml')
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        MDVP_Fo=st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVP_Fhi=st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVP_Flo=st.text_input('MDVP:Flo(Hz)')
    with col4:
        MDVP_Jitter_per=st.text_input('MDVP:Jitter(%)')
    with col5:
        MDVP_Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
    with col1:
        MDVP_RAP=st.text_input('MDVP:RAP')
    with col2:
        MDVP_PPQ=st.text_input('MDVP:PPQ')
    with col3:
        Jitter_DDP=st.text_input('Jitter:DDP')
    with col4:
        MDVP_Shimmer=st.text_input('MDVP:Shimmer')
    with col5:
        MDVP_Shimmer_dB=st.text_input('MDVP:Shimmer(dB)')
    with col1:
        Shimmer_APQ3=st.text_input('Shimmer:APQ3')
    with col2:
        Shimmer_APQ5=st.text_input('Shimmer:APQ5')
    with col3:
        MDVP_APQ=st.text_input('MDVP:APQ')
    with col4:
        Shimmer_DDA=st.text_input('Shimmer:DDA')
    with col5:
        NHR=st.text_input('NHR')
    with col1:
        HNR=st.text_input('HNR')
    with col2:
        RPDE=st.text_input('RPDE')
    with col3:
        DFA=st.text_input('DFA')
    with col4:
        spread1=st.text_input('Spread1')
    with col5:
        spread2=st.text_input('Spread2')
    with col1:
        D2=st.text_input('D2')
    with col2:
        PPE=st.text_input('PPE')

    parkinsons_diagnosis=''

    if st.button('Parkinsons Test Result'):
        user_input=[MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_Jitter_per,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,
                    Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        user_input=[float(x) for x in user_input]
        parkinsons_prediction=parkinsons_model.predict([user_input])
        if parkinsons_prediction[0]==1:
            parkinsons_diagnosis='The person has parkinsons.'
        else:
            parkinsons_diagnosis='The person is not having parkinsons.'
    st.success(parkinsons_diagnosis)