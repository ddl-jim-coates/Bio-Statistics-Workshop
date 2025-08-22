# Clinical Trial Adverse Event Prediction Workshop
This workshop provides biostatisticians and clinical researchers with hands-on experience using the Domino Data Lab platform for predictive modeling in clinical trials. Participants will work through the complete model development lifecycle, from exploratory data analysis to deploying a model that predicts serious adverse events (SAEs) in clinical trial patients.

## Exercises
Below are the exercises attendees will complete as part of the workshop.  The exercise directories correspond with each exercise and include all resources needed to complete the exercise including instructions, slides, notebooks, and scripts.  Each exercise builds upon the other.  As such they must be completed in sequential order:

### 1 - Up & Running
Set up the clinical research environment. Configure data access permissions and collaboration settings for your research team.
  
### 2 - Clinical Data Exploration 
Interactive analysis of clinical trial data using Jupyter notebooks. Load patient data from S3, perform quality checks, visualize patient demographics and baseline characteristics, and save cleaned dataset for analysis. 

### 3 - Clinical Feature Engineering
Automated feature engineering pipeline for clinical data. Create derived clinical features (risk scores, adherence metrics, biomarker ratios), apply statistical transformations, and prepare data for machine learning models.

### 4 - Predictive Model Training & Validation
Train multiple models (XGBoost, AdaBoost, Naive Bayes) to predict adverse events. Evaluate model performance using clinical metrics (sensitivity, specificity, PPV, NPV). Assess model fairness across patient subgroups.

Select and register the best-performing model for deployment.

### 5 - Clinical Decision Support Deployment
- REST APIs for real-time risk scoring
- Web application for clinician-facing adverse event risk assessment
- Automated monitoring dashboards for patient safety

## Use Case: Clinical Trial Safety Monitoring

This workshop simulates a real-world scenario where a pharmaceutical company needs to identify patients at high risk of serious adverse events during a multi-site clinical trial. The predictive model helps:

- **Patient Safety**: Early identification of at-risk patients for enhanced monitoring
- **Resource Allocation**: Optimize clinical staff time by focusing on high-risk patients
- **Regulatory Compliance**: Demonstrate proactive safety monitoring to regulatory bodies
- **Trial Success**: Reduce dropout rates by preventing adverse events

## Dataset Description

The synthetic clinical trial dataset includes:
- **Patient Demographics**: Age, BMI, generation cohort
- **Medical History**: Years with condition, comorbidity scores, prior medications
- **Clinical Measurements**: Baseline biomarkers, genetic risk scores, treatment adherence
- **Trial Information**: Treatment arm, visit type, site category
- **Geographic Data**: Site location, distance from primary care
- **Outcome**: Adverse event occurrence (binary classification target)

The dataset mimics real clinical trial data with ~0.7% adverse event rate, reflecting the challenge of predicting rare but critical events.
