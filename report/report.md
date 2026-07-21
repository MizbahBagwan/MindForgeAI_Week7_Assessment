# Early Academic Support System

## Machine Learning Based Student Academic Risk Prediction

---

# 1. Executive Summary

The Early Academic Support System is a machine learning based application designed to identify students who may require additional academic support. The objective of this project is to help teachers and counselors detect early warning signs and provide timely interventions.

The system uses student demographic, academic, family, and behavioral information to predict academic risk. The prediction output helps educational stakeholders prioritize students who may benefit from additional guidance.

This system is designed as a decision-support tool and should not replace human judgement.

---

# 2. Problem Statement

Students may face academic difficulties due to multiple factors such as:

* Low previous grades
* High absence rate
* Previous failures
* Limited study time
* Lack of academic support
* Social and family factors

Early identification of risk can allow schools to provide appropriate support before academic performance declines significantly.

---

# 3. Stakeholder and Operational Decision

## Stakeholder

Primary stakeholders:

* Teachers
* Academic counselors
* School administrators

## Operational Decision

The system supports the decision:

"Which students may need additional academic attention or intervention?"

The prediction is used to prioritize support activities such as:

* Counseling
* Extra learning support
* Academic mentoring

---

# 4. Machine Learning Task

## Task Type

Binary Classification

## Target Variable

Academic_Risk

Values:

* 0 → Student not identified as high risk
* 1 → Student may require academic support

## Unit of Analysis

One row represents one student's academic and personal information.

---

# 5. Dataset Description

## Dataset Source

Student Performance Dataset (UCI Machine Learning Repository)

Dataset contains information about:

* Student demographics
* Family background
* School support
* Study habits
* Previous grades
* Absences
* Social factors

## Dataset Size

Total Records:

395 students

Total Features:

33 original attributes

---

# 6. Data Preparation

Steps performed:

* Loaded dataset
* Checked missing values
* Checked duplicate records
* Reviewed data types
* Identified categorical and numerical features
* Removed target leakage

## Data Quality Findings

* Missing values: None
* Duplicate rows: None
* Categorical features: Present
* Numerical features: Present

---

# 7. Exploratory Data Analysis (EDA)

Important observations:

## Finding 1

Students with previous failures show higher academic risk.

Impact:
Previous failures were included as an important predictive feature.

---

## Finding 2

Low grades in previous assessments are associated with increased risk.

Impact:
Previous academic performance was considered during modeling.

---

## Finding 3

Higher absence rates are linked with increased academic difficulty.

Impact:
Absence information was included.

---

## Finding 4

Study time influences academic performance.

Impact:
Study habits were included as model features.

---

## Finding 5

Family and school support can influence student outcomes.

Impact:
Support-related features were retained.

---

# 8. Data Splitting Strategy

Dataset was divided into:

Training Data:
80%

Testing Data:
20%

The split was performed using stratification to maintain class distribution.

---

# 9. Feature Engineering and Preprocessing

The following preprocessing pipeline was used:

## Numerical Features

Processing:

* Standard Scaling

Examples:

* Age
* Study time
* Absences
* Grades

## Categorical Features

Processing:

* One Hot Encoding

Examples:

* School
* Gender
* Parent job
* Support information

All preprocessing steps were included inside the ML pipeline to prevent data leakage.

---

# 10. Model Development

## Algorithm Used

Gradient Boosting Classifier

Reason for selection:

* Handles complex relationships
* Works well with mixed feature types
* Provides strong classification performance

---

# 11. Model Evaluation

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

Evaluation was performed on unseen test data.

---

# 12. Deployment

The trained model was deployed using Streamlit.

Application Features:

* User-friendly interface
* Student information input
* Academic risk prediction
* Risk probability display
* Support recommendation message

---

# 13. Responsible AI Considerations

## Limitations

* Prediction depends on dataset quality.
* Model may not represent every school environment.
* Human judgement is required before taking action.

## Appropriate Use

The model should be used for:

* Early identification
* Support prioritization
* Academic counseling assistance

The model should not be used for:

* Punishment
* Student exclusion
* Automated decisions without human review

---

# 14. Project Structure

```
EarlyAcademicSupport/

├── data/
│   └── student-mat.csv

├── notebooks/
│   ├── EDA.ipynb
│   └── 02_modeling.ipynb

├── models/
│   └── student_risk_model.pkl

├── app/
│   └── app.py

├── reports/
│   └── final_report.pdf

├── README.md
└── requirements.txt
```

---

# 15. Conclusion

The Early Academic Support System demonstrates how machine learning can assist educational decision-making by identifying students who may require additional academic support.

The developed system combines data analysis, machine learning, and deployment into a practical application.

Future improvements include:

* Testing on larger datasets
* Adding more student history data
* Continuous model monitoring
* Improving explainability using feature importance methods

---

# Final Recommendation

The system can be used as a support tool for educators to identify students who may benefit from early intervention.

Final decisions should always involve teachers, counselors, and educational experts.
