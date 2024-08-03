import streamlit as st
from streamlit_option_menu import option_menu
import sys
import os
from PIL import Image


# Get the parent directory of the current script
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

# Now you can import the target file using an absolute import
from general_conditions import general_conditions_backendfunction as gen
from diabetes import diabetes_backendfunction as diab
from skin_diseases import skin_diseases_backendfunction as skin


#streamlit app*******************************************************************************************************************************************
def main():
    # Set page configuration
    st.set_page_config(page_title="Health Assistant",
                    layout="wide",
                    page_icon="🧑‍⚕️")


    # sidebar for navigation
    with st.sidebar:
        selected = option_menu('Multiple Disease Detection System',

                            ['Symptom based Detection',
                                'Diabetes Detection',
                                'Skin Disease Detection'],
                            menu_icon='hospital-fill',
                            icons=['activity', 'heart','bandaid-fill'],
                            default_index=0)



    # Diabetes Prediction Page
    if selected == 'Symptom based Detection':
            
            # Streamlit
            st.title("Symptom based Medical Condition Detector")
            st.write("Enter a paragraph describing your symptoms, and the model will detect possible medical conditions along with their definitions and recommendations.")

            # Input from user
            symptoms = st.text_area("Describe your symptoms here:")

            if st.button("Predict"):
                if symptoms:

                    # Get predictions from the model
                    result= gen.give_predicted_result(symptoms)
                    # return {"predicted_disease":predicted_disease,
                    #          "confidence_score":confidence_score,
                    #          "description":description,
                    #          "recommendations":recommendations}

                    
                    if result== None or result['confidence_score']  < .45 :
                        st.write("Please describe the symptoms clearly and in more detail")

                    else:
                        # Display the results
                            st.write("### Detected Medical Condition")
                            st.write(f"**Medical Condition:** {result['predicted_disease']}")
                            st.write(f"**Confidence (approx):** {result['confidence_score'] * 100:.2f}% &nbsp; &nbsp;&nbsp;&nbsp;**(This confidence score reflects the reliability of the result)**")
                            st.write(f"**Definition:** {result['description']}")
                            
                            st.write("**Recommendations:**")
                            for recommendation in result['recommendations']:
                                st.write(f"- {recommendation}")     
                else:
                    st.write("Please enter a description of your symptoms.")



    #Diabetes Prediction Page
    if selected == 'Diabetes Detection':
        st.title('Diabetes Detector')

        # Input fields for diabetes prediction
        pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0, step=1)
        glucose = st.number_input("Glucose", min_value=0, max_value=200, value=0, step=1)
        blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=150, value=0, step=1)
        skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=0, step=1)
        insulin = st.number_input("Insulin", min_value=0, max_value=900, value=0, step=1)
        bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=0.0, step=0.1)
        diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.0, step=0.01)
        age = st.number_input("Age", min_value=0, max_value=120, value=0, step=1)

        if st.button("Predict Diabetes"):
            if( [glucose,blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]==[0,0,0,0,0.00,0.00,0]) :
                    st.write("Please enter details properly")

            else:
                # Get predictions from the diabetes model
                result = diab.give_diabetes_prediction([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age])
                
                # Display the result
                st.write("### Prediction Result")
                st.write(f"Prediction: {result['predicted_class']}")
                st.write(f"Confidence: {result['confidence']} % &nbsp; &nbsp;&nbsp;&nbsp; **(This confidence score reflects the reliability of the result)**")


    #Skin Disease Prediction Page
    if selected == 'Skin Disease Detection':

            st.title("Skin Disease Detector")
            st.write("Upload an image...")

            # File uploader widget
            uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

            if uploaded_file is not None:

                # Display the uploaded image
                image = Image.open(uploaded_file)
                st.image(image, caption='Uploaded Image.', width=400)

                # Predict button
                if st.button('Predict'):
                        # Make prediction on the uploaded image
                        prediction = skin.give_skin_diseases_prediction(uploaded_file)

                        st.write(f"Prediction: {prediction['predicted_class']}")
                        st.write(f"Confidence: {prediction['confidence']} %&nbsp; &nbsp;&nbsp;&nbsp; **(This confidence score reflects the reliability of the result)**")


if __name__ == '__main__':
    main()