# Beyond the Books
### Can a Student's Wellbeing predict Academic Success as well as their Study Hours?

A data science project by Emma Reeb — UAL, Software Development with Big Data and Cloud (2026)

Unit Leader: Marissa Beaty

---

## Project Overview

This project investigates whether a student's **wellbeing** can predict their final grade as effectively as the number of hours they study. Rather than treating academic success as a simple product of study time, this project argues that grades emerge from a broader, intersectional system of student behaviour and circumstance.

A composite **Wellbeing Index** is constructed from three variables — `sleep_hours`, `exercise_minutes`, and `stress_level` — and its correlation with `final_grade` is compared against that of `study_hours_per_day` using the Pearson correlation formula.

---

## Dataset

**Student Productivity & Digital Distraction Dataset**  
Source: [Kaggle](https://www.kaggle.com/datasets/sehaj1104/student-productivity-and-digital-distraction-dataset/data)

- 20,000 rows, 18 columns
- Each row represents one student
- No missing values
- Key columns used: `exercise_minutes`, `sleep_hours`, `stress_level`, `study_hours_per_day`, `final_grade`

> **Note:** Analysis revealed all correlations with `final_grade` to be near zero across every variable. This strongly suggests the dataset is synthetically generated, with grades assigned independently of all other variables. This is acknowledged as a core limitation and discussed in the findings.

---

## Methodology

### 1. Wellbeing Index Construction
Each component is normalised to a 0–1 scale using min-max scaling. `stress_level` is inverted since higher stress contributes negatively to wellbeing. The three normalised values are averaged with equal weighting:

```
wellbeing_score = (exercise_norm + sleep_norm + (1 - stress_norm)) / 3
```

### 2. Correlation Analysis
Pearson correlation coefficients are calculated between:
- `wellbeing_score` and `final_grade`
- `study_hours_per_day` and `final_grade`

### 3. Visualisations
- Scatter plots for each predictor vs `final_grade`
- Correlation heatmap across all five key variables
- Bar chart comparing average grade across low, medium and high wellbeing groups

---

## Findings

| Predictor | Correlation | P-value |
|---|---|---|
| `study_hours_per_day` | -0.0122 | 0.0843 |
| `wellbeing_score` | 0.0119 | 0.0928 |

Neither predictor shows a statistically significant relationship with `final_grade` (both p-values > 0.05). This is consistent across all 18 variables in the dataset, suggesting synthetic data generation rather than a real-world null result. The methodology is sound and would be directly applicable to a verified academic dataset.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Core language |
| Pandas | Data loading and manipulation |
| SciPy | Pearson correlation |
| Matplotlib & Seaborn | Visualisation |
| Conda | Environment management |
| Google Cloud Storage | Remote dataset hosting |
| VS Code | Development environment |
| Claude Code | Explanation of Concepts, help generating Algorithm, Cloud/Bucket interaction |

---

## Project Structure

```
student-wellbeing/
├── analysis.ipynb          # Full analysis: wellbeing index, correlation, visualisations
├── cloud_data.py           # Google Cloud Storage connection and data loading
├── .env                    # GCP credentials (not committed)
├── .gitignore              # Excludes .env, .csv, __pycache__ etc.
├── environment.yml         # Conda environment — reproduce with: conda env create -f environment.yml
└── README.md
```

---

## Setup & Reproduction

**1. Clone the repository**
```bash
git clone <your-repo-url>
cd student-wellbeing
```

**2. Recreate the conda environment**
```bash
conda env create -f environment.yml
conda activate wellbeing
```

**3. Add your GCP credentials**

Create a `.env` file in the project root:
```
GCP_PROJECT_ID=your-project-id
GCP_BUCKET_NAME=your-bucket-name
```

Then authenticate:
```bash
gcloud auth application-default login
```

**4. Run the analysis**

Open `analysis.ipynb` in VS Code and run all cells.

---

## Limitations

- The dataset originates from an individual Kaggle contributor with no documented collection methodology — findings cannot be generalised
- The Wellbeing Index uses equal weighting across its three components — a subjective choice that could influence results
- Pearson correlation detects only linear relationships — non-linear patterns would not be captured

---

## Author

Emma Reeb 
UAL — Software Development with Big Data and Cloud  

