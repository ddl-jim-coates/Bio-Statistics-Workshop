import os
import streamlit as st
import time
import random
import pandas as pd
import numpy as np
import requests
# Import add_derived_features function
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'c_DataEngineering'))
from data_engineering import add_derived_features

feature_scaling_endpoint = os.environ['feature_scaling_endpoint']
feature_scaling_auth = os.environ['feature_scaling_auth']

xgboost_endpoint = os.environ['xgboost_endpoint']
xgboost_auth = os.environ['xgboost_auth']

adaboost_endpoint = os.environ['adaboost_endpoint']
adaboost_auth = os.environ['adaboost_auth']

gaussiannb_endpoint = os.environ['gaussiannb_endpoint']
gaussiannb_auth = os.environ['gaussiannb_auth']

model_scaling_dict = {
    'XG Boost': {
        'endpoint': xgboost_endpoint,
        'auth': xgboost_auth,
    },
    'ADA Boost': {
        'endpoint': adaboost_endpoint,
        'auth': adaboost_auth,
    },
    'GaussianNB': {
        'endpoint': gaussiannb_endpoint,
        'auth': gaussiannb_auth,
    }
}

# Define schema once at module level
CLASSIFIER_SCHEMA = [
    'num__Time', 'num__BMI', 'num__Age', 'num__YearsWithCondition', 'num__ComorbidityScore',
    'num__Adherence', 'num__PriorMedications', 'num__BaselineBiomarker', 'num__GeneticRisk',
    'num__Latitude', 'num__Longitude', 'num__DistanceFromCare', 'num__VisitHour',
    'num__InPerson', 'num__bmi_biomarker_ratio', 'num__clinical_risk_score',
    'num__adherence_risk_balance', 'cat__TreatmentArm_high_dose', 'cat__TreatmentArm_low_dose',
    'cat__TreatmentArm_placebo', 'cat__TreatmentArm_standard_dose', 'cat__VisitType_baseline',
    'cat__VisitType_followup', 'cat__VisitType_screening', 'cat__VisitType_week_12',
    'cat__VisitType_week_4', 'cat__SiteCategory_academic_medical', 'cat__SiteCategory_community_hospital',
    'cat__SiteCategory_private_practice', 'cat__SiteCategory_research_center', 'cat__SiteCategory_specialty_clinic',
    'cat__SiteCategory_university_hospital', 'cat__SiteCategory_va_hospital', 'cat__SiteCategory_regional_medical',
    'cat__CollectionMethod_ePRO', 'cat__CollectionMethod_home_visit', 'cat__CollectionMethod_in_person',
    'cat__CollectionMethod_telemedicine', 'cat__Generation_Baby Boomer', 'cat__Generation_Generation X',
    'cat__Generation_Generation Z', 'cat__Generation_Millennial', 'cat__Generation_Silent Generation'
]


def scaled_data_to_classifier_format(scaled_data):
    """Convert scaled data array to classifier input format"""
    values = scaled_data[0]  # First (and only) row
    
    # Dynamically create the dictionary using zip
    classifier_data = dict(zip(CLASSIFIER_SCHEMA, values))
    return classifier_data
    

def create_patient_data(bmi, visit_hour, treatment_arm, in_person, age, years_condition, 
                       prior_meds, baseline_biomarker, comorbidity_score, adherence, 
                       genetic_risk, distance_care, latitude, longitude, 
                       visit_type, site_category, collection_method):
    """Create a single-row DataFrame with clinical patient data"""
    
    # Days since enrollment (simulate current trial day)
    days_enrolled = random.uniform(1, 365)
    
    # Create clinical patient data matching expected structure
    patient_data = {
        'Time': days_enrolled,
        'BMI': bmi,
        'Age': age,
        'YearsWithCondition': years_condition,
        'ComorbidityScore': comorbidity_score,
        'Adherence': adherence,
        'PriorMedications': prior_meds,
        'BaselineBiomarker': baseline_biomarker,
        'GeneticRisk': genetic_risk,
        'Latitude': latitude,
        'Longitude': longitude,
        'DistanceFromCare': distance_care,
        'VisitHour': visit_hour,
        'TreatmentArm': treatment_arm,
        'VisitType': visit_type,
        'SiteCategory': site_category,
        'CollectionMethod': collection_method,
        'InPerson': in_person
    }
    
    # Create DataFrame
    df = pd.DataFrame([patient_data])
    
    # Add derived clinical features
    df_with_features = add_derived_features(df)
    
    return df_with_features



st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🔒",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .prediction-box {
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin: 2rem 0;
    }
    .fraud-alert {
        background-color: #ff4b4b;
        color: white;
        border: 2px solid #ff0000;
    }
    .safe-alert {
        background-color: #00cc88;
        color: white;
        border: 2px solid #00aa66;
    }
    .stButton > button {
        background-color: #1f77b4;
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        border-radius: 5px;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🏥 Clinical Trial Adverse Event Risk Assessment</h1>', unsafe_allow_html=True)

# Add model selection dropdown
st.subheader("🧬 Predictive Model Selection")
selected_model = st.selectbox(
    "Choose Risk Prediction Model",
    options=list(model_scaling_dict.keys()),
    index=2  # Default to GaussianNB
)

# Create three columns for better layout
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📊 Clinical Measurements")
    amount = st.number_input("BMI", min_value=15.0, value=26.5, step=0.1)
    hour = st.selectbox("Visit Hour", range(8, 18), index=2)
    tx_type = st.selectbox("Treatment Arm", ["placebo", "low_dose", "standard_dose", "high_dose"])
    card_present = st.selectbox("In-Person Visit", [0, 1], format_func=lambda x: "Yes" if x else "No")

with col2:
    st.subheader("👤 Patient Demographics")
    age = st.slider("Age", 18, 85, 55)
    tenure = st.slider("Years with Condition", 0, 30, 5)
    txn_24h = st.number_input("Prior Medications", min_value=0, value=3, step=1)
    avg_30d = st.number_input("Baseline Biomarker", value=25.0, step=0.1)

with col3:
    st.subheader("⚠️ Risk Indicators")
    merchant_risk = st.slider("Comorbidity Score", 0.0, 10.0, 3.0, 0.1)
    device_trust = st.slider("Treatment Adherence %", 0.0, 100.0, 85.0, 1.0)
    ip_reputation = st.slider("Genetic Risk Score", 0.0, 100.0, 20.0, 1.0)
    dist_from_home = st.slider("Distance from Care (km)", 0.0, 200.0, 20.0, 1.0)

# Clinical site and visit details
st.subheader("🏥 Clinical Site & Visit")
col4, col5 = st.columns(2)

with col4:
    latitude = st.number_input("Site Latitude", value=40.0, step=0.01)
    longitude = st.number_input("Site Longitude", value=-75.0, step=0.01)
    
with col5:
    device_type = st.selectbox("Visit Type", ["screening", "baseline", "week_4", "week_12", "followup"])
    merchant_cat = st.selectbox("Site Category", 
                               ["academic_medical", "community_hospital", "specialty_clinic", "research_center", "private_practice"])
    channel = st.selectbox("Collection Method", ["in_person", "telemedicine", "home_visit", "ePRO"])

# Prediction button and results
st.markdown("---")
predict_button = st.button("🔬 Assess Adverse Event Risk", type="primary")

if predict_button:
    # Show loading spinner
    with st.spinner("Analyzing patient data... 🔬"):
        time.sleep(2)  # Simulate API call

        
        # Create the patient data with derived clinical features
        patient_df = create_patient_data(
            bmi=amount,  # amount variable maps to BMI
            visit_hour=hour,
            treatment_arm=tx_type,
            in_person=card_present,
            age=age,
            years_condition=tenure,
            prior_meds=txn_24h,
            baseline_biomarker=avg_30d,
            comorbidity_score=merchant_risk,
            adherence=device_trust,
            genetic_risk=ip_reputation,
            distance_care=dist_from_home,
            latitude=latitude,
            longitude=longitude,
            visit_type=device_type,
            site_category=merchant_cat,
            collection_method=channel
        )
        
        print("Here's the patient data we have:")
        print(patient_df.to_dict('records')[0])
        
        # Create JSON structure for clinical API
        patient_json = {
            "data": {
                "Time": str(patient_df['Time'].iloc[0]),
                "BMI": str(patient_df['BMI'].iloc[0]),
                "Age": str(patient_df['Age'].iloc[0]),
                "YearsWithCondition": str(patient_df['YearsWithCondition'].iloc[0]),
                "ComorbidityScore": str(patient_df['ComorbidityScore'].iloc[0]),
                "Adherence": str(patient_df['Adherence'].iloc[0]),
                "PriorMedications": str(patient_df['PriorMedications'].iloc[0]),
                "BaselineBiomarker": str(patient_df['BaselineBiomarker'].iloc[0]),
                "GeneticRisk": str(patient_df['GeneticRisk'].iloc[0]),
                "Latitude": str(patient_df['Latitude'].iloc[0]),
                "Longitude": str(patient_df['Longitude'].iloc[0]),
                "DistanceFromCare": str(patient_df['DistanceFromCare'].iloc[0]),
                "VisitHour": str(patient_df['VisitHour'].iloc[0]),
                "TreatmentArm": patient_df['TreatmentArm'].iloc[0],
                "VisitType": patient_df['VisitType'].iloc[0],
                "SiteCategory": patient_df['SiteCategory'].iloc[0],
                "CollectionMethod": patient_df['CollectionMethod'].iloc[0],
                "InPerson": str(patient_df['InPerson'].iloc[0]),
                "bmi_biomarker_ratio": str(round(patient_df['bmi_biomarker_ratio'].iloc[0], 2)),
                "clinical_risk_score": str(round(patient_df['clinical_risk_score'].iloc[0], 2)),
                "adherence_risk_balance": str(round(patient_df['adherence_risk_balance'].iloc[0], 2)),
                "Generation": patient_df['Generation'].iloc[0]
            }
        }

        scaled_transaction = None
        fraud_prediction = None

        # Make API call for input scaling
        try:
            response = requests.post(
                feature_scaling_endpoint,
                auth=(
                    feature_scaling_auth,
                    feature_scaling_auth
                ),
                json=transaction_json
            )
            
            if response.status_code == 200:
                resp = response.json()
                scaled_transaction = resp['result']
                print('scaled_transaction = ')
                print(scaled_transaction)

                # Convert scaled data to classifier format
                classifier_input = scaled_data_to_classifier_format(scaled_transaction)
                print('classifier_input = ')
                print(classifier_input)

                # Get selected model endpoint and auth
                selected_endpoint = model_scaling_dict[selected_model]['endpoint']
                selected_auth = model_scaling_dict[selected_model]['auth']

                # Make API call to selected classifier
                try:
                    classifier_response = requests.post(
                        selected_endpoint,
                        auth=(selected_auth, selected_auth),
                        json={"data": classifier_input}
                    )
                    
                    if classifier_response.status_code == 200:
                        classifier_resp = classifier_response.json()
                        print('resp')
                        print(classifier_resp)
                        fraud_prediction = classifier_resp['result']
                        print('fraud_prediction = ')
                        print(fraud_prediction)
                    else:
                        st.error(f"Classifier API Error: {classifier_response.status_code}")
                        print(f"Classifier error: {classifier_response.text}")
                        
                except requests.exceptions.RequestException as e:
                    st.error(f"Classifier Connection Error: {str(e)}")


                
            else:
                st.error(f"API Error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            st.error(f"Connection Error: {str(e)}")

        
        
        # Clinical risk assessment logic (demo purposes)
        final_risk_score = random.uniform(0, 1)
        
        # Clinical risk factors for adverse events
        risk_factors = [
            amount > 30,  # BMI > 30 (obesity)
            merchant_risk > 5.0,  # High comorbidity score
            device_trust < 70.0,  # Low adherence
            ip_reputation > 40.0,  # High genetic risk
            dist_from_home > 50.0,  # Far from care facility
            tx_type == "high_dose"  # High dose treatment
        ]
        
        final_risk_score = sum(risk_factors) / len(risk_factors)
        is_adverse_event = final_risk_score > 0.4
        
        # Display clinical risk assessment results
        if is_adverse_event:
            st.markdown(f"""
            <div class="prediction-box fraud-alert">
                <h2>⚠️ HIGH RISK PATIENT</h2>
                <h3>Adverse Event Risk: {final_risk_score:.2%}</h3>
                <p>This patient has elevated risk for serious adverse events.</p>
                <p>Recommend enhanced monitoring and safety protocols.</p>
                <p><strong>Model Used:</strong> {selected_model}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="prediction-box safe-alert">
                <h2>✅ LOW RISK PATIENT</h2>
                <h3>Adverse Event Risk: {final_risk_score:.2%}</h3>
                <p>This patient shows low risk for adverse events.</p>
                <p>Standard monitoring protocols appropriate.</p>
                <p><strong>Model Used:</strong> {selected_model}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Show clinical risk factors breakdown
        st.subheader("📊 Clinical Risk Factor Analysis")
        
        risk_data = {
            "Factor": ["BMI > 30", "High Comorbidity", "Low Adherence", "Genetic Risk", "Distance from Care", "High Dose"],
            "Value": [f"{amount:.1f}", f"{merchant_risk:.1f}", f"{device_trust:.0f}%", f"{ip_reputation:.0f}", f"{dist_from_home:.0f} km", tx_type],
            "Status": ["⚠️" if factor else "✅" for factor in risk_factors]
        }
        
        df = pd.DataFrame(risk_data)
        st.dataframe(df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666;'>🏥 Clinical Trial Safety Assessment v1.0 | Built with Streamlit</p>",
    unsafe_allow_html=True
)