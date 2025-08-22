# Clinical Trial Adaptation Guide

## Overview
This workshop has been adapted from a fraud detection use case to predict **Serious Adverse Events (SAEs)** in clinical trials. The adaptation maintains the same technical infrastructure while using clinically relevant terminology and metrics.

## Use Case: Clinical Trial Safety Monitoring

### Business Context
- **Original**: Detect fraudulent credit card transactions
- **Adapted**: Predict patients at risk for serious adverse events in clinical trials

### Why This Matters for Biostatisticians
- Direct application to Phase II/III clinical trials
- Addresses real regulatory requirements (FDA, EMA safety monitoring)
- Uses standard biostatistical metrics (sensitivity, specificity, PPV, NPV)
- Incorporates clinical trial design considerations

## Data Mapping

### Column Translations
The data structure maintains compatibility with original code through strategic naming:

| Clinical Meaning | Variable Name | Original Meaning | Clinical Range |
|-----------------|---------------|------------------|----------------|
| Days since enrollment | Time | Transaction time | 0-365 days |
| Body Mass Index | Amount/BMI | Transaction amount | 16-45 |
| Patient age | Age | Customer age | 18-85 years |
| Years with condition | Tenure | Account tenure | 0-30 years |
| Comorbidity score | MerchantRisk | Merchant risk | 0-10 scale |
| Treatment adherence % | DeviceTrust | Device trust score | 0-100% |
| Prior medications count | Txn24h | Recent transactions | 0-15 |
| Baseline biomarker level | Avg30d | 30-day average | 5-100 units |
| Genetic risk score | IPReputation | IP reputation | 0-100 |
| Distance from care (km) | DistFromHome | Distance from home | 0-200 km |
| Visit hour | Hour | Transaction hour | 8-17 |
| In-person visit flag | CardPresent | Card present flag | 0/1 |
| **Adverse Event** | Class | Fraud flag | 0/1 |

### Categorical Variables

#### Treatment Arms (TxType)
- `placebo` - Control group
- `low_dose` - Low dose treatment
- `standard_dose` - Standard dose treatment  
- `high_dose` - High dose treatment

#### Visit Types (DeviceType)
- `screening` - Initial screening visit
- `baseline` - Baseline measurements
- `week_4` - 4-week follow-up
- `week_12` - 12-week follow-up
- `followup` - General follow-up

#### Site Categories (MerchantCat)
- `academic_medical` - Academic medical centers
- `community_hospital` - Community hospitals
- `specialty_clinic` - Specialty clinics
- `research_center` - Dedicated research centers
- `private_practice` - Private practice sites

#### Collection Methods (Channel)
- `in_person` - Traditional in-person visit
- `telemedicine` - Remote consultation
- `home_visit` - Home health visit
- `ePRO` - Electronic patient-reported outcomes

## Derived Features

### Clinical Risk Scores
1. **BMI-Biomarker Ratio** (`amount_vs_avg30d_ratio`)
   - Identifies metabolic imbalance patterns
   - Higher ratios indicate potential metabolic dysfunction

2. **Composite Risk Score** (`risk_score`)
   - Combines comorbidity burden and genetic predisposition
   - Normalized 0-1 scale for model input

3. **Adherence-Comorbidity Balance** (`trust_score`)
   - Positive: Good adherence despite comorbidities
   - Negative: Poor adherence with high comorbidity burden

## Model Interpretation

### Metrics Translation
| Clinical Metric | Code Variable | Interpretation |
|----------------|---------------|----------------|
| Sensitivity | recall_adverse | % of adverse events correctly identified |
| Specificity | 1 - FPR | % of safe patients correctly identified |
| PPV | precision_adverse | % of high-risk predictions that are correct |
| NPV | - | % of low-risk predictions that are correct |
| AUROC | roc_auc | Overall discriminative ability |

### Clinical Decision Thresholds
- **High Sensitivity Mode** (>0.95): Maximize adverse event detection
- **Balanced Mode** (0.85): Balance between sensitivity and specificity
- **High Specificity Mode** (>0.95): Minimize false alarms

## Minimal Code Changes Required

### Files to Update for Full Clinical Context

1. **Exercise Instructions** (`exercises/*/instructions.md`)
   - Update terminology from fraud to clinical context
   - Add clinical interpretation guidance

2. **Notebook Markdown Cells** (`exercises/b_DataExploration/*.ipynb`)
   - Update descriptions to clinical context
   - Add clinical significance explanations

3. **Model API Descriptions**
   - Update endpoint documentation
   - Add clinical use case examples

### Files That Work As-Is
- All Python training scripts (column names are mapped)
- Data pipeline code (uses mapped names)
- Model evaluation code (metrics are universal)
- Streamlit app structure (UI text updated)

## Data Generation

### Creating Synthetic Clinical Data
```bash
# Generate synthetic clinical trial data
python generate_clinical_data.py

# This creates:
# - data/clinical_trial_data.csv (with clinical column names)
# - data/clean_cc_transactions.csv (compatible with existing code)
# - data/test_clinical_data.csv (smaller test dataset)
```

### Uploading to S3
1. Upload `clean_cc_transactions.csv` to your S3 bucket
2. Use the same path structure as original workshop
3. Data will be automatically recognized by the pipeline

## Clinical Scenarios Simulated

### Patient Risk Factors for Adverse Events
- **Demographics**: Older age (>65), multiple comorbidities
- **Treatment**: High dose, poor adherence (<70%)
- **Genetics**: High genetic risk score (>40)
- **Access**: Far from care facility (>50km)
- **History**: Many prior medications (>5)

### Expected Outcomes
- Adverse event rate: ~0.7% (mimics rare event detection)
- Model performance: AUROC 0.85-0.92 expected
- Clinical utility: 90% sensitivity at 20% false positive rate

## Workshop Learning Objectives (Clinical Context)

1. **Exploratory Data Analysis**
   - Understand patient population characteristics
   - Identify risk factor distributions
   - Visualize adverse event patterns

2. **Feature Engineering**
   - Create clinically meaningful derived features
   - Handle missing clinical data appropriately
   - Standardize biomarker measurements

3. **Model Development**
   - Train multiple models for comparison
   - Optimize for clinical metrics (sensitivity vs specificity)
   - Validate on held-out patient cohorts

4. **Clinical Deployment**
   - Deploy risk scoring API for real-time assessment
   - Build clinician-facing dashboard
   - Implement safety monitoring alerts

## Regulatory Considerations

### Model Documentation
- Maintain audit trail via MLflow
- Document feature importance for interpretability
- Track model versions for regulatory submissions

### Patient Safety
- Emphasize high sensitivity for safety-critical applications
- Include confidence intervals in predictions
- Flag high-risk patients for enhanced monitoring

### Bias Assessment
- Evaluate model fairness across:
  - Age groups
  - Treatment arms
  - Site categories
  - Geographic regions

## Next Steps for Full Implementation

1. **Required**: Run `generate_clinical_data.py` to create datasets
2. **Required**: Upload data to S3 bucket
3. **Optional**: Update exercise markdown files for complete clinical context
4. **Optional**: Add clinical-specific visualizations
5. **Optional**: Implement additional clinical metrics (NNT, time-to-event)

## Support Resources

### Clinical Trial Terminology
- **SAE**: Serious Adverse Event requiring hospitalization or causing disability
- **AE**: Any unfavorable medical occurrence
- **Protocol Deviation**: Departure from approved study protocol
- **ITT**: Intention-to-treat analysis population
- **Per Protocol**: Analysis of compliant patients only

### Statistical Methods
- **Logistic Regression**: Baseline clinical prediction model
- **XGBoost**: Captures non-linear clinical interactions
- **Naive Bayes**: Assumes feature independence (simplified model)

### Regulatory Guidelines
- FDA Guidance on Safety Monitoring
- ICH E6 Good Clinical Practice
- CDISC Standards for clinical data