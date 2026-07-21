# Model Card - Early Academic Support System

## Model Overview

### Model Name
Student Academic Risk Prediction Model

### Purpose
The model predicts whether a student may need early academic support.

### ML Task
Binary Classification

Target:
- 1 = Needs Support
- 0 = No Support


---

## Stakeholders

Primary users:

- Teachers
- School administrators
- Academic counselors


---

## Dataset

Dataset:
Student Performance Dataset (UCI)

Unit of Analysis:
One row represents one student's academic record.


---

## Features Used

The model uses:

- Demographic information
- Study habits
- Family information
- Academic behavior
- Absences


Features removed:

- G3 (Final Grade)

Reason:
G3 is the prediction target and would cause data leakage.


---

## Model

Algorithm:

Random Forest Classifier


Pipeline:

1. Missing value handling
2. Numerical feature scaling
3. Categorical encoding
4. Classification model


---

## Evaluation Metrics

Primary Metric:

Recall

Reason:
Missing a student who needs help (False Negative) has higher cost.


Additional Metrics:

- Precision
- F1 Score
- Accuracy


---

## Error Analysis

False Positive:

A student is predicted as high risk but does not need support.

Impact:
Extra support resources may be used.


False Negative:

A student is predicted safe but actually needs support.

Impact:
Student may not receive timely intervention.


---

## Limitations

- Dataset size is small.
- Data comes from specific schools.
- Model performance may reduce on different populations.
- Predictions should support human decisions, not replace teachers.


---

## Responsible Use

The model should:

- Assist teachers in identifying students who may need attention.
- Be reviewed by human experts.
- Not be used for punishment or exclusion decisions.


---

## Deployment Status

Model is saved as:

models/student_risk_model.pkl