"""
Generate Synthetic Clinical Trial Data for Adverse Event Prediction

This script generates realistic synthetic clinical trial data with patient characteristics,
medical history, lab values, and adverse event outcomes. The data structure mirrors
the original fraud detection dataset to minimize code changes.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

def generate_clinical_trial_data(n_samples=100000):
    """
    Generate synthetic clinical trial data with realistic distributions
    """
    
    # Define adverse event rate (similar to fraud rate ~0.5%)
    adverse_event_rate = 0.007
    n_adverse = int(n_samples * adverse_event_rate)
    n_normal = n_samples - n_adverse
    
    data = []
    
    # Treatment arms (similar to transaction types)
    treatment_arms = ['placebo', 'low_dose', 'standard_dose', 'high_dose']
    
    # Site categories (similar to merchant categories)
    site_categories = ['academic_medical', 'community_hospital', 'specialty_clinic', 
                      'research_center', 'private_practice', 'va_hospital', 
                      'university_hospital', 'regional_medical']
    
    # Visit types (similar to device types)
    visit_types = ['screening', 'baseline', 'week_4', 'week_12', 'followup']
    
    # Data collection methods (similar to channels)
    collection_methods = ['in_person', 'telemedicine', 'home_visit', 'ePRO']
    
    # Generate normal patients (no adverse events)
    for i in range(n_normal):
        # Time since enrollment (days) - similar to transaction time
        time_enrolled = np.random.uniform(0, 365)
        
        # Age with realistic distribution
        age = np.random.normal(55, 15)
        age = np.clip(age, 18, 85)
        
        # BMI - important clinical metric (similar to Amount)
        bmi = np.random.normal(27, 5)
        bmi = np.clip(bmi, 16, 45)
        
        # Years with condition (similar to Tenure)
        years_with_condition = np.random.exponential(5)
        years_with_condition = np.clip(years_with_condition, 0, 30)
        
        # Comorbidity score (0-10 scale, similar to MerchantRisk)
        comorbidity_score = np.random.beta(2, 5) * 10
        
        # Treatment adherence (0-100%, similar to DeviceTrust)
        adherence = np.random.beta(9, 2) * 100
        
        # Number of prior medications (similar to Txn24h)
        prior_medications = np.random.poisson(3)
        
        # Baseline lab value (e.g., biomarker level, similar to Avg30d)
        baseline_biomarker = np.random.lognormal(3, 0.5)
        baseline_biomarker = np.clip(baseline_biomarker, 5, 100)
        
        # Genetic risk score (0-100, similar to IPReputation)
        genetic_risk = np.random.beta(2, 8) * 100
        
        # Geographic coordinates for site
        latitude = np.random.uniform(25, 48)
        longitude = np.random.uniform(-125, -65)
        
        # Distance from primary care (km, similar to DistFromHome)
        distance_from_care = np.random.exponential(20)
        distance_from_care = np.clip(distance_from_care, 0, 200)
        
        # Visit hour (24-hour format)
        visit_hour = np.random.choice(range(8, 18), p=[0.05, 0.1, 0.15, 0.15, 0.15, 0.15, 0.1, 0.1, 0.05, 0.0])
        
        # In-person visit flag (similar to CardPresent)
        in_person = 1 if np.random.random() > 0.2 else 0
        
        # Select categorical variables
        treatment_arm = np.random.choice(treatment_arms)
        site_category = np.random.choice(site_categories)
        visit_type = np.random.choice(visit_types)
        collection_method = np.random.choice(collection_methods, 
                                           p=[0.6, 0.2, 0.1, 0.1] if in_person else [0.1, 0.6, 0.2, 0.1])
        
        # Age generation (similar to card generation in original)
        if age < 35:
            generation = 'Millennial'
        elif age < 45:
            generation = 'Generation X'
        elif age < 65:
            generation = 'Baby Boomer'
        else:
            generation = 'Silent Generation'
        
        data.append({
            'Time': time_enrolled,
            'BMI': round(bmi, 1),
            'Age': int(age),
            'YearsWithCondition': round(years_with_condition, 1),
            'ComorbidityScore': round(comorbidity_score, 2),
            'Adherence': round(adherence, 1),
            'PriorMedications': prior_medications,
            'BaselineBiomarker': round(baseline_biomarker, 2),
            'GeneticRisk': round(genetic_risk, 2),
            'Latitude': round(latitude, 4),
            'Longitude': round(longitude, 4),
            'DistanceFromCare': round(distance_from_care, 1),
            'VisitHour': visit_hour,
            'InPerson': in_person,
            'TreatmentArm': treatment_arm,
            'VisitType': visit_type,
            'SiteCategory': site_category,
            'CollectionMethod': collection_method,
            'Generation': generation,
            'AdverseEvent': 0  # No adverse event
        })
    
    # Generate patients with adverse events
    for i in range(n_adverse):
        time_enrolled = np.random.uniform(0, 365)
        
        # Adverse event patients tend to be older
        age = np.random.normal(62, 12)
        age = np.clip(age, 18, 85)
        
        # Higher BMI associated with adverse events
        bmi = np.random.normal(30, 6)
        bmi = np.clip(bmi, 16, 50)
        
        # Longer disease duration
        years_with_condition = np.random.exponential(7)
        years_with_condition = np.clip(years_with_condition, 0, 35)
        
        # Higher comorbidity scores
        comorbidity_score = np.random.beta(5, 3) * 10
        
        # Lower adherence
        adherence = np.random.beta(6, 4) * 100
        
        # More prior medications
        prior_medications = np.random.poisson(5)
        
        # Abnormal biomarker levels
        baseline_biomarker = np.random.lognormal(3.5, 0.7)
        baseline_biomarker = np.clip(baseline_biomarker, 5, 150)
        
        # Higher genetic risk
        genetic_risk = np.random.beta(5, 5) * 100
        
        latitude = np.random.uniform(25, 48)
        longitude = np.random.uniform(-125, -65)
        
        # May be further from care
        distance_from_care = np.random.exponential(30)
        distance_from_care = np.clip(distance_from_care, 0, 250)
        
        # Irregular visit times might indicate issues
        visit_hour = np.random.choice(range(7, 19))
        
        # Less likely to be in-person (might indicate health issues)
        in_person = 1 if np.random.random() > 0.35 else 0
        
        # Higher doses more likely to have adverse events
        treatment_arm = np.random.choice(treatment_arms, p=[0.15, 0.2, 0.3, 0.35])
        site_category = np.random.choice(site_categories)
        visit_type = np.random.choice(visit_types)
        collection_method = np.random.choice(collection_methods)
        
        if age < 35:
            generation = 'Millennial'
        elif age < 45:
            generation = 'Generation X'
        elif age < 65:
            generation = 'Baby Boomer'
        else:
            generation = 'Silent Generation'
        
        data.append({
            'Time': time_enrolled,
            'BMI': round(bmi, 1),
            'Age': int(age),
            'YearsWithCondition': round(years_with_condition, 1),
            'ComorbidityScore': round(comorbidity_score, 2),
            'Adherence': round(adherence, 1),
            'PriorMedications': prior_medications,
            'BaselineBiomarker': round(baseline_biomarker, 2),
            'GeneticRisk': round(genetic_risk, 2),
            'Latitude': round(latitude, 4),
            'Longitude': round(longitude, 4),
            'DistanceFromCare': round(distance_from_care, 1),
            'VisitHour': visit_hour,
            'InPerson': in_person,
            'TreatmentArm': treatment_arm,
            'VisitType': visit_type,
            'SiteCategory': site_category,
            'CollectionMethod': collection_method,
            'Generation': generation,
            'AdverseEvent': 1  # Adverse event occurred
        })
    
    # Create DataFrame and shuffle
    df = pd.DataFrame(data)
    df = df.sample(frac=1).reset_index(drop=True)
    
    return df

def create_column_mapping():
    """
    Create a mapping between clinical and original column names
    to minimize code changes
    """
    mapping = {
        'Time': 'Time',  # Days since enrollment
        'BMI': 'Amount',  # BMI maps to Amount
        'Age': 'Age',
        'YearsWithCondition': 'Tenure',  # Years with condition maps to Tenure
        'ComorbidityScore': 'MerchantRisk',  # Comorbidity maps to risk
        'Adherence': 'DeviceTrust',  # Adherence maps to trust
        'PriorMedications': 'Txn24h',  # Prior meds maps to recent transactions
        'BaselineBiomarker': 'Avg30d',  # Baseline biomarker maps to average
        'GeneticRisk': 'IPReputation',  # Genetic risk maps to reputation
        'Latitude': 'Latitude',
        'Longitude': 'Longitude',
        'DistanceFromCare': 'DistFromHome',  # Distance from care
        'VisitHour': 'Hour',  # Visit hour
        'InPerson': 'CardPresent',  # In-person visit maps to card present
        'TreatmentArm': 'TxType',  # Treatment arm maps to transaction type
        'VisitType': 'DeviceType',  # Visit type maps to device type
        'SiteCategory': 'MerchantCat',  # Site category maps to merchant category
        'CollectionMethod': 'Channel',  # Collection method maps to channel
        'Generation': 'generation',
        'AdverseEvent': 'Class'  # Adverse event maps to fraud class
    }
    return mapping

def main():
    """
    Generate and save clinical trial datasets
    """
    print("Generating synthetic clinical trial data...")
    
    # Generate main dataset
    df_clinical = generate_clinical_trial_data(n_samples=100000)
    
    # Create mapped version for code compatibility
    mapping = create_column_mapping()
    df_mapped = df_clinical.rename(columns={v: k for k, v in mapping.items() if k != v})
    
    # For compatibility, rename columns to match original structure
    df_compat = df_clinical.copy()
    for clinical_col, original_col in mapping.items():
        if clinical_col in df_compat.columns:
            df_compat = df_compat.rename(columns={clinical_col: original_col})
    
    # Save datasets
    output_dir = 'data'
    os.makedirs(output_dir, exist_ok=True)
    
    # Save clinical version (with descriptive names)
    df_clinical.to_csv(f'{output_dir}/clinical_trial_data.csv', index=False)
    print(f"✓ Saved clinical trial data: {output_dir}/clinical_trial_data.csv")
    
    # Save compatible version (for minimal code changes)
    df_compat.to_csv(f'{output_dir}/clean_cc_transactions.csv', index=False)
    print(f"✓ Saved compatible data: {output_dir}/clean_cc_transactions.csv")
    
    # Generate smaller dataset for testing
    df_test = generate_clinical_trial_data(n_samples=10000)
    for clinical_col, original_col in mapping.items():
        if clinical_col in df_test.columns:
            df_test = df_test.rename(columns={clinical_col: original_col})
    df_test.to_csv(f'{output_dir}/test_clinical_data.csv', index=False)
    print(f"✓ Saved test dataset: {output_dir}/test_clinical_data.csv")
    
    # Print statistics
    print("\nDataset Statistics:")
    print(f"Total samples: {len(df_clinical):,}")
    print(f"Adverse events: {df_clinical['AdverseEvent'].sum():,} ({df_clinical['AdverseEvent'].mean()*100:.2f}%)")
    print(f"Normal cases: {(1-df_clinical['AdverseEvent']).sum():,}")
    print(f"Features: {len(df_clinical.columns) - 1}")
    
    # Save column mapping documentation
    with open(f'{output_dir}/column_mapping.txt', 'w') as f:
        f.write("Clinical Column -> Code Column Mapping\n")
        f.write("=" * 40 + "\n\n")
        for clinical, original in mapping.items():
            f.write(f"{clinical:20} -> {original}\n")
    print(f"\n✓ Saved column mapping: {output_dir}/column_mapping.txt")
    
    return df_clinical

if __name__ == "__main__":
    df = main()
    print("\n✅ Data generation complete!")
    print("\nNext steps:")
    print("1. Upload clean_cc_transactions.csv to your S3 bucket")
    print("2. The code will work with minimal changes due to compatible column names")
    print("3. UI text and documentation will need updates for clinical context")