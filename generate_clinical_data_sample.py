"""
Sample of Clinical Trial Data Structure
This shows what the generated data will look like
"""

import json

# Sample data structure
sample_data = {
    "clinical_columns": [
        "Time",  # Days since enrollment (0-365)
        "BMI",  # Body Mass Index (16-45)
        "Age",  # Patient age (18-85)
        "YearsWithCondition",  # Years with primary condition (0-30)
        "ComorbidityScore",  # Comorbidity index (0-10)
        "Adherence",  # Treatment adherence percentage (0-100)
        "PriorMedications",  # Number of prior medications (0-15)
        "BaselineBiomarker",  # Baseline biomarker level (5-100)
        "GeneticRisk",  # Genetic risk score (0-100)
        "Latitude",  # Clinical site latitude
        "Longitude",  # Clinical site longitude
        "DistanceFromCare",  # Distance from primary care (km)
        "VisitHour",  # Hour of visit (8-17)
        "InPerson",  # In-person visit flag (0/1)
        "TreatmentArm",  # placebo/low_dose/standard_dose/high_dose
        "VisitType",  # screening/baseline/week_4/week_12/followup
        "SiteCategory",  # Type of clinical site
        "CollectionMethod",  # in_person/telemedicine/home_visit/ePRO
        "Generation",  # Age generation category
        "AdverseEvent"  # Target variable (0=No, 1=Yes)
    ],
    
    "mapped_columns": {
        "Time": "Time",
        "BMI": "Amount",
        "Age": "Age",
        "YearsWithCondition": "Tenure",
        "ComorbidityScore": "MerchantRisk",
        "Adherence": "DeviceTrust",
        "PriorMedications": "Txn24h",
        "BaselineBiomarker": "Avg30d",
        "GeneticRisk": "IPReputation",
        "Latitude": "Latitude",
        "Longitude": "Longitude",
        "DistanceFromCare": "DistFromHome",
        "VisitHour": "Hour",
        "InPerson": "CardPresent",
        "TreatmentArm": "TxType",
        "VisitType": "DeviceType",
        "SiteCategory": "MerchantCat",
        "CollectionMethod": "Channel",
        "Generation": "generation",
        "AdverseEvent": "Class"
    },
    
    "sample_patient_normal": {
        "Time": 142.5,
        "BMI": 26.3,
        "Age": 52,
        "YearsWithCondition": 4.2,
        "ComorbidityScore": 3.1,
        "Adherence": 89.5,
        "PriorMedications": 3,
        "BaselineBiomarker": 22.4,
        "GeneticRisk": 18.7,
        "Latitude": 40.7128,
        "Longitude": -74.0060,
        "DistanceFromCare": 15.3,
        "VisitHour": 10,
        "InPerson": 1,
        "TreatmentArm": "standard_dose",
        "VisitType": "week_12",
        "SiteCategory": "academic_medical",
        "CollectionMethod": "in_person",
        "Generation": "Generation X",
        "AdverseEvent": 0
    },
    
    "sample_patient_adverse": {
        "Time": 87.3,
        "BMI": 31.8,
        "Age": 68,
        "YearsWithCondition": 8.7,
        "ComorbidityScore": 6.8,
        "Adherence": 72.3,
        "PriorMedications": 7,
        "BaselineBiomarker": 48.9,
        "GeneticRisk": 52.1,
        "Latitude": 34.0522,
        "Longitude": -118.2437,
        "DistanceFromCare": 42.7,
        "VisitHour": 15,
        "InPerson": 0,
        "TreatmentArm": "high_dose",
        "VisitType": "week_4",
        "SiteCategory": "community_hospital",
        "CollectionMethod": "telemedicine",
        "Generation": "Baby Boomer",
        "AdverseEvent": 1
    }
}

print("Clinical Trial Data Structure Preview")
print("=" * 50)
print("\nColumn Mapping (Clinical -> Code Compatible):")
for clinical, code in sample_data["mapped_columns"].items():
    print(f"  {clinical:20} -> {code}")

print("\n\nSample Normal Patient (No Adverse Event):")
print(json.dumps(sample_data["sample_patient_normal"], indent=2))

print("\n\nSample Patient with Adverse Event:")
print(json.dumps(sample_data["sample_patient_adverse"], indent=2))

print("\n\nData Characteristics:")
print("- Total samples: 100,000")
print("- Adverse event rate: ~0.7% (similar to rare event detection)")
print("- Features: 19 (mix of continuous and categorical)")
print("- Realistic clinical distributions and correlations")