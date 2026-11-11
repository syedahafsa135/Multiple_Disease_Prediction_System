# 🩺 Multiple Disease Prediction System

![Diabetes prediction page of the Streamlit app](images/app-diabetes.jpg)

![Heart disease prediction page of the Streamlit app](images/app-heart.jpg)

A Streamlit web app that estimates **diabetes** and **heart disease** risk from routine health measurements, using two trained machine learning classifiers.

**Portfolio:** [syedahafsa135.github.io](https://syedahafsa135.github.io)

---

## Problem

**Can a few routine measurements, such as glucose, BMI, blood pressure and cholesterol, flag patients who may need further testing for diabetes or heart disease?**

## Data

| Dataset | File | Rows | Target split |
|---|---|---|---|
| Diabetes | `data_models/diabetes.csv` | 768 patients, 8 features | 500 not diabetic, 268 diabetic |
| Heart disease | `data_models/heart_disease_data.csv` | 303 patients, 13 features | 138 no disease, 165 disease |

## Method

**Diabetes** (`Diabetes_Prediction.ipynb`)
1. EDA: distributions, box plots, and z-score outlier counts per feature
2. Standardise the features with `StandardScaler`
3. Stratified 80/20 split (614 train / 154 test)
4. Train a **linear Support Vector Machine**

**Heart disease** (`Heart_Disease_Prediction.ipynb`)
1. EDA: distributions of age, sex, chest pain type, cholesterol, ECG results and more
2. 80/20 split (242 train / 61 test)
3. Train **logistic regression**

Both models are saved in `sav_files/` and served in the Streamlit app (`Multiple disease Prediction System.py`).

## Results

| Model | Test accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Diabetes (linear SVM) | 0.773 | 0.757 | 0.519 | 0.615 |
| Heart disease (logistic regression) | 0.885 | 0.879 | 0.906 | 0.892 |

- **The heart model is the stronger screen.** It caught about 9 in 10 heart disease cases in the 61-patient test set. That test set is small, though, so the result should be confirmed with cross-validation.
- **The diabetes model misses about half of diabetic patients** (recall 0.519), even though its accuracy looks reasonable. For a screening tool, recall matters more than accuracy, so the next step is to tune for recall, for example with class weights or a lower decision threshold.

Source: `Diabetes_Prediction.ipynb` cells 50–51 and `Heart_Disease_Prediction.ipynb` cells 70 and 72.

## How to run

```bash
git clone https://github.com/syedahafsa135/Multiple_Disease_Prediction_System.git
cd Multiple_Disease_Prediction_System
python -m venv venv
venv\Scripts\activate          # on Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
streamlit run "Multiple disease Prediction System.py"
```

The notebooks were written for Google Colab. To re-run them, open them in Colab and change the `read_csv` paths to the files in `data_models/`.

## Limitations

- Small test sets (61 heart patients, 154 diabetes patients): confirm the scores with cross-validation.
- The diabetes model's recall of 0.519 is too low for screening; tune for recall (class weights or a lower threshold) first.
- Both algorithms were also implemented from scratch for comparison (see Report.pdf); the app uses the scikit-learn versions.

## Project structure

```
├── Multiple disease Prediction System.py   # Streamlit app
├── Diabetes_Prediction.ipynb               # EDA + SVM training
├── Heart_Disease_Prediction.ipynb          # EDA + logistic regression training
├── data_models/                            # the two datasets
├── sav_files/                              # trained models
├── background_pic/                         # app background images
└── Report.pdf                              # project report
```

## Tech stack

Python · pandas · NumPy · scikit-learn · Matplotlib · Seaborn · Streamlit

> ⚠️ For learning purposes only. This app is not a medical diagnosis tool.
