# 🏭 Manufacturing Equipment Output Prediction (End-to-End ML Application)

## 📌 Overview
This project is an end-to-end Machine Learning application that predicts the hourly production output (Parts Per Hour) of manufacturing injection molding machines based on operational parameters such as temperature, pressure, cycle time, machine age, and material properties.

The system includes:
- Machine Learning model training
- REST API using FastAPI
- Interactive frontend using Streamlit
- Cloud deployment of backend and frontend

---

## 🎯 Problem Statement
Manufacturing companies need to optimize machine parameters to improve productivity and reduce downtime.  
This application predicts machine output using historical operating data, helping engineers make data-driven decisions.

---

## 🧠 Solution
A supervised learning regression model (Linear Regression) is trained on historical machine data.  
The trained model is exposed via a FastAPI backend and consumed by a Streamlit frontend for real-time predictions.

---

## 🗂 Dataset
- Name: manufacturing_dataset_1000_samples.csv  
- Records: 1000  
- Target Variable: Parts_Per_Hour  
- Input Features:
  - Injection_Temperature  
  - Injection_Pressure  
  - Cycle_Time  
  - Cooling_Time  
  - Material_Viscosity  
  - Ambient_Temperature  
  - Machine_Age  
  - Operator_Experience  
  - Maintenance_Hours  
  - Shift  
  - Machine_Type  
  - Material_Grade  
  - Day_of_Week  

---

## 🛠 Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- FastAPI  
- Streamlit  
- Joblib  
- Git & GitHub  
- Render (Backend Deployment)  
- Streamlit Cloud (Frontend Deployment)

---

## ⚙ ML Pipeline
1. Data Cleaning  
2. Feature Engineering  
3. Encoding Categorical Features  
4. Feature Scaling  
5. Train-Test Split  
6. Model Training (Linear Regression)  
7. Model Evaluation  
8. Model Serialization  

---

## 🚀 Live Application

### Frontend:
https://manufacturing-ml-app-kbckuwpprzlgzhlsfaljsw.streamlit.app/

### Backend API:
https://manufacturing-ml-app.onrender.com/docs

---

## 📁 Project Structure

manufacturing_ml_project  
│  
├── backend  
│   ├── app.py  
│   └── requirements.txt  
│  
├── frontend  
│   ├── app.py  
│  
├── model  
│   └── manufacturing_model.pkl  
│  
├── data  
│   └── manufacturing_dataset_1000_samples.csv  
│  
└── README.md  

---

## ▶ Run Locally

### Backend

cd backend  
python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  
uvicorn app:app --reload  

### Frontend

cd frontend  
python -m venv venv  
venv\Scripts\activate  
pip install streamlit requests  
streamlit run app.py  

---

## 📈 Results
The model provides reliable predictions for manufacturing output based on machine operating conditions, enabling better optimization of production settings.

---

## 👤 Author
Faiz Ahmed Khan  
