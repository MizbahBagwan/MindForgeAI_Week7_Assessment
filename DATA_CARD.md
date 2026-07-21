# Data Card - Student Performance Dataset

## Dataset Name
Student Performance Dataset (UCI)

## Source
UCI Machine Learning Repository

## Owner
University of California, Irvine (UCI) Machine Learning Repository

## Dataset Purpose
The dataset contains student demographic, social and academic information to study factors affecting student performance.

## Data Type
Structured tabular dataset.

## Unit of Analysis
One row represents one student.

## Original Schema

Main features include:

- school
- sex
- age
- address
- famsize
- Pstatus
- Medu
- Fedu
- studytime
- failures
- paid
- activities
- internet
- romantic
- famrel
- freetime
- goout
- health
- absences
- G1
- G2
- G3

## Target Variable

G3 - Final Grade

For ML:

Academic_Risk

Transformation:

G3 < 10  → Risk = 1

G3 >= 10 → Risk = 0


## License

Open dataset for educational and research purposes.

## Privacy

No direct personal identifiers are included.

## Limitations

- Dataset size is small.
- Data represents students from specific schools.
- Results may not generalize to all education systems.