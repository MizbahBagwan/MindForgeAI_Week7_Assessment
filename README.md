# Early Academic Support System

## Problem Framing

### Stakeholder
School administrators, teachers and academic counselors.

### Operational Decision
Identify students who may need early academic support such as mentoring, counseling, or extra classes.

### Unit of Analysis
One row represents one student's academic record.

### ML Task
Classification.

### Target
Academic_Risk

Rule:
- G3 < 10 → Risk = 1 (Needs Support)
- G3 >= 10 → Risk = 0 (No Support)

### Prediction Horizon
Before final grade is available.

### Information Available at Decision Time
- Student demographics
- Study habits
- Family information
- Previous academic information
- Absences

### Error Cost

False Positive:
Student marked at risk but actually not at risk.
Cost: Extra support resources used.

False Negative:
Student not identified but actually needs help.
Cost: Student may fail without intervention.

### Success Metric
Primary:
Recall

Secondary:
F1-score and PR-AUC

### Baseline
Majority class classifier.
