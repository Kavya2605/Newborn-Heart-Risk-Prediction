# 🫀 Newborn Heart Risk Prediction System

## 1. Project Overview

The **Newborn Heart Risk Prediction System** is an educational Machine
Learning and Streamlit application for classifying newborn health/heart
risk into three categories:

-   **Healthy**
-   **At Risk**
-   **High Risk**

The application accepts newborn parameters through a Streamlit interface
and uses a **Random Forest Classifier** to generate the predicted risk
level.

## 2. Objectives

1.  Develop a Machine Learning model for newborn risk-level
    classification.
2.  Use relevant newborn demographic and physiological parameters.
3.  Preprocess numerical and categorical data.
4.  Train and evaluate a Random Forest classifier.
5.  Save the trained model for later prediction.
6.  Build an interactive Streamlit interface.
7.  Display a simple Healthy / At Risk / High Risk result.
8.  Provide a foundation for future work with validated clinical
    datasets.

## 3. Technologies

  Technology      Purpose
  --------------- ----------------------
  Python          Programming
  Pandas          Data handling
  Scikit-learn    Machine Learning
  Random Forest   Classification
  Joblib          Model saving/loading
  Streamlit       Web interface
  Matplotlib      Visualization
  Seaborn         Exploratory analysis
  CSV             Dataset storage

## 4. Project Structure

``` text
newborn_heart_risk_project/
│
├── app.py
├── model.py
├── newborn_heart_risk_10000.csv
├── newborn_risk_model.pkl
├── requirements.txt
├── README.md
│
└── plots/
    ├── risk_level_distribution.png
    ├── heart_rate_vs_spo2.png
    └── correlation_heatmap.png
```

### File Description

-   **app.py** --- Streamlit interface and prediction logic.
-   **model.py** --- Loads data, preprocesses features, trains/evaluates
    the model, and saves it.
-   **newborn_heart_risk_10000.csv** --- Synthetic dataset containing
    10,000 newborn records.
-   **newborn_risk_model.pkl** --- Saved trained ML pipeline.
-   **requirements.txt** --- Required Python packages.
-   **README.md** --- Project documentation.

## 5. Dataset

The project uses a synthetic dataset containing **10,000 newborn
records**.

### Main Features

  Feature                     Description
  --------------------------- ------------------------------------
  Sex                         Newborn sex
  Gestational_Age_weeks       Gestational age in weeks
  Birth_Weight_kg             Birth weight
  Heart_Rate_bpm              Heart rate
  Respiratory_Rate_bpm        Respiratory rate
  Oxygen_Saturation_percent   Oxygen saturation
  Feeding_Frequency_per_day   Feeding frequency
  Urine_Output_Count          Urine output count
  Jaundice_Level_mg_dL        Jaundice level
  Temperature_C               Temperature
  Apgar_Score                 Apgar score
  Oxygen_Given                Whether oxygen was given
  Resuscitation_Required      Whether resuscitation was required

### Target

The target variable is:

``` text
Risk_Level
```

Classes:

``` text
Healthy
At Risk
High Risk
```

## 6. Machine Learning Workflow

``` text
Dataset
   ↓
Data Loading
   ↓
Feature Selection
   ↓
Preprocessing
   ↓
Train/Test Split
   ↓
Random Forest Classifier
   ↓
Model Evaluation
   ↓
Save Model
   ↓
Streamlit Application
   ↓
User Input
   ↓
Risk Prediction
```

## 7. Data Preprocessing

The project uses a Scikit-learn preprocessing pipeline.

### Categorical Data

The `Sex` feature contains categorical values such as:

``` text
Female
Male
```

It is converted using **OneHotEncoder**.

### Numerical Data

The health measurements are handled as numerical features.

The preprocessing and classifier are combined in one pipeline so that
the same transformation is used during training and prediction.

## 8. Machine Learning Algorithm

The project uses a **Random Forest Classifier**.

Example configuration:

``` python
RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)
```

### Parameters

-   `n_estimators=200` --- 200 decision trees.
-   `random_state=42` --- reproducible training.
-   `class_weight="balanced"` --- helps account for class imbalance.

## 9. Train-Test Split

The dataset is divided into:

``` text
80% → Training
20% → Testing
```

Stratification is used so that the risk classes are represented in both
sets.

## 10. Model Evaluation

The training script reports:

-   Accuracy
-   Precision
-   Recall
-   F1-score
-   Classification report

The actual values depend on the dataset and training run.

## 11. Streamlit Interface

The application contains:

### Header

``` text
🫀 Newborn Heart Risk Predictor
Enter the newborn's details below to predict the heart risk level.
```

### Newborn Details

The interface uses a clean two-column layout and includes:

-   Gestational Age
-   Birth Weight
-   Heart Rate
-   Respiratory Rate
-   Oxygen Saturation
-   Temperature
-   Feeding Frequency
-   Apgar Score
-   Urine Output
-   Jaundice Level
-   Sex
-   Oxygen Given
-   Resuscitation Required

### Prediction

The user selects or enters the values and clicks:

``` text
📊 Predict Heart Risk Level
```

The application sends the input to the trained model.

## 12. Prediction Output

The application displays:

``` text
💚 Healthy
```

or:

``` text
⚠️ At Risk
```

or:

``` text
🚨 High Risk
```

The result is displayed in a dedicated result card.

## 13. Data Visualization

Recommended exploratory plots include:

1.  **Risk Level Distribution** --- number of records in each target
    class.
2.  **Heart Rate vs Oxygen Saturation** --- relationship between two
    important physiological variables.
3.  **Correlation Heatmap** --- correlations among numerical features.

## 14. Installation

### Step 1 --- Check Python

``` bash
python --version
```

### Step 2 --- Open the project folder

``` bash
cd path/to/newborn_heart_risk_project
```

### Step 3 --- Install dependencies

``` bash
pip install -r requirements.txt
```

If necessary:

``` bash
python -m pip install -r requirements.txt
```

## 15. Train the Model

Run:

``` bash
python model.py
```

This creates:

``` text
newborn_risk_model.pkl
```

## 16. Run the Streamlit Application

Run:

``` bash
streamlit run app.py
```

If the command is not recognized:

``` bash
python -m streamlit run app.py
```

The application normally opens at:

``` text
http://localhost:8501
```

Do **not** start a Streamlit application using:

``` bash
python app.py
```

## 17. How to Use

1.  Start the Streamlit application.
2.  Enter the newborn's details.
3.  Select Sex.
4.  Select Oxygen Given.
5.  Select Resuscitation Required.
6.  Click **Predict Heart Risk Level**.
7.  View the predicted risk category.

## 18. Example Input

``` text
Gestational Age      : 37.5 weeks
Birth Weight         : 2.76 kg
Heart Rate           : 145 bpm
Respiratory Rate     : 30 bpm
Oxygen Saturation    : 93 %
Temperature          : 37.3 °C
Apgar Score          : 10
Feeding Frequency    : 9/day
Urine Output         : 8/day
Jaundice Level       : 2.8 mg/dL
Sex                  : Female
Oxygen Given         : No
Resuscitation        : No
```

The model returns one of:

``` text
Healthy
At Risk
High Risk
```

## 19. Troubleshooting

### `ModuleNotFoundError`

Run:

``` bash
pip install -r requirements.txt
```

### `FileNotFoundError: newborn_risk_model.pkl`

Train the model first:

``` bash
python model.py
```

### `missing ScriptRunContext`

Use:

``` bash
streamlit run app.py
```

instead of:

``` bash
python app.py
```

### Dropdown appears with a black background

The dropdown styling is controlled by the custom CSS in `app.py`. The
`selectbox` CSS can be modified in the `<style>` section near the top of
the file.

## 20. Limitations

-   The model has not been clinically validated.
-   Predictions are not medical diagnoses.
-   Real neonatal data may contain many additional variables.
-   Real clinical deployment would require validated data, external
    validation, medical expert review, and appropriate regulatory
    processes.

## 21. Future Enhancements

Possible improvements include:

-   Use validated real-world neonatal datasets.
-   Add additional clinically relevant variables.
-   Compare Random Forest with Logistic Regression, SVM, XGBoost, and
    other models.
-   Add confusion matrix visualization.
-   Add ROC-AUC and precision-recall analysis where appropriate.
-   Add feature-importance visualization.
-   Add SHAP-based explainability.
-   Add prediction history.
-   Generate downloadable reports.
-   Improve responsive/mobile design.
-   Perform external validation.

## 22. Advantages

-   Simple user interface
-   Interactive Streamlit application
-   Machine Learning-based classification
-   Fast prediction
-   Easy-to-understand output
-   Reusable preprocessing/model pipeline
-   Visualization support
-   Easy to extend with future datasets

## 23. Conclusion

The **Newborn Heart Risk Prediction System** demonstrates the
integration of Machine Learning, data preprocessing, visualization, and
Streamlit into one application.

The system accepts newborn health parameters, processes them through a
trained Random Forest model, and produces a simple risk-level
classification:

``` text
Healthy | At Risk | High Risk
```

The project is suitable as an academic demonstration and as a foundation
for future development using validated neonatal data.

## 24. Disclaimer

**This application is intended only for educational and
software-development purposes. The dataset used in this project is
synthetic. The predictions are not clinically validated and must not be
used to diagnose, treat, or make healthcare decisions for newborns. Real
clinical deployment would require appropriate medical validation,
regulatory review, and qualified healthcare professionals.**
