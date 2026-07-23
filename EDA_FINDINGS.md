# EDA Findings - Student Performance Dataset

## 1. Dataset Overview

- Dataset contains 395 student records.
- Each row represents one student's academic and personal information.
- Dataset contains demographic, social, study-related and academic features.
- Target variable: G3 (Final Grade)

---

## 2. Finding: Previous Grades are Strong Predictors

Observation:
- G1 and G2 show strong relationship with final grade G3.

Impact on Modeling:
- Previous grades can improve prediction performance.
- Their usage depends on the prediction time.
- If grades are not available at decision time, they must be removed to avoid leakage.

---

## 3. Finding: Study Time Influences Performance

Observation:
- Students with higher study time generally show better academic performance.

Impact on Modeling:
- Study time should be included as an important feature.

---

## 4. Finding: Previous Failures Increase Academic Risk

Observation:
- Students with more previous failures tend to have lower final grades.

Impact on Modeling:
- Failures is an important risk indicator.
- Feature should be included.

---

## 5. Finding: Absences Affect Performance

Observation:
- Higher absence levels show relationship with lower grades.

Impact on Modeling:
- Absences should be included as a predictive feature.

---

## 6. Finding: Class Distribution

Observation:
- Academic risk classes may not be perfectly balanced.

Impact on Modeling:
- Use appropriate evaluation metrics:
  - Recall
  - F1-score
  - PR-AUC