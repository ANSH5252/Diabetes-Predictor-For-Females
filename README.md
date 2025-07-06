# 🩺 Diabetes Predictor for Females

A **machine learning-powered web application** that predicts whether a female is likely to have diabetes based on several health parameters. Built using **Streamlit** and trained on the **Pima Indians Diabetes Dataset**, this app enables users to interactively input data and get real-time predictions.

## 🚀 Features

- 🧠 ML model trained with multiple classifiers
- 🧪 Accuracy and precision comparison across models
- 🧰 Hyperparameter tuning using `GridSearchCV`
- 🖼️ User-friendly interface built with Streamlit
- ⚡ Real-time diabetes prediction

## 📊 Tech Stack

**Language**: Python 🐍

**Libraries Used**:

- `pandas`, `numpy` – Data manipulation  
- `scikit-learn` – Model training, evaluation, preprocessing  
- `streamlit` – Front-end for the web application  
- `pickle` – Model serialization  
- `xgboost` – For additional model experiments

**Techniques Used**:

- Decision Tree Classification  
- Standardization with `StandardScaler`  
- Model performance tuning with `GridSearchCV`  
- Stratified train-test splitting  
- Voting Classifier ensemble (optional)

## 📁 Project Structure
```
Diabetes-Predictor-For-Females
│
├── app.py            # Main Streamlit app file
├── diabetes.csv      # Dataset used for training
├── model.pkl         # Trained Decision Tree model
├── scaler.pkl        # Fitted StandardScaler object
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
└── .gitignore        # Files ignored by Git
```

## 📁 Dataset Used

- **Name** : Pima Indians Diabetes Database  
- **Source** : [Kaggle - Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Features** :
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age
  - Outcome (0 = No Diabetes, 1 = Diabetes)

## 🖥️ How to Run

- 📥 Clone the Repository

```
git clone https://github.com/ANSH5252/Diabetes-Predictor-For-Females.git
cd Diabetes-Predictor-For-Females
```
- 🛠️ Install Dependencies
```
pip install -r requirements.txt
```
- 🚀 Launch the Streamlit App
```
streamlit run app.py
```

## 🧠 How It Works
- ✅ Data Preprocessing
  - Dataset: diabetes.csv (Pima Indians Diabetes Database)

  - Target column: Outcome (1 = diabetic, 0 = non-diabetic)

  - Features include: Glucose, Insulin, BMI, Age, etc.

  - Data is standardized using StandardScaler

- ✅ Model Building & Training
  - Multiple models tested: SVC, KNN, Logistic Regression, Random Forest, XGBoost, etc.

  - Final model: DecisionTreeClassifier with optimal hyperparameters

  - Trained using train_test_split with stratification

  - Accuracy and precision evaluated on test set

  - Saved using pickle

- ✅ App Workflow
  - User inputs values from the sidebar

  - Values are scaled using the trained scaler.pkl

  - Prediction is made using model.pkl

  - Output is displayed as either:
  - 🟥 Diabetes Detected or 🟩 No Diabetes

## 🖼️ App UI
- 📌 Sidebar inputs
- 📌 Main screen result with clear visual feedback
- 📌 User is prompted if prediction hasn’t been triggered yet

## 🧪 Example Usage
- Open the app using streamlit run app.py

- Enter sample inputs in the sidebar:
  - Pregnancies : 1,
  - Glucose : 148, 
  - Blood Pressure : 100,
  - Skin Thickness : 70,
  - Insulin : 15,
  - BMI : 50.00, 
  - Diabetes Pedigree Function : 2.50,
  - Age : 50

- Click on Predict

- Result will display instantly as :

  - ❌ “The model predicts that the individual **has diabetes**.”

## 📸 Screenshots
- **Initial Interface** :

![Screenshot 2025-07-05 122819](https://github.com/user-attachments/assets/e045048c-2b8d-49ed-8517-7523b322b1d1)

- **Interface when Diabetes is not Detected** :

![Screenshot 2025-07-05 122844](https://github.com/user-attachments/assets/17f9249e-53f4-4f28-a05e-9b3b207ea0dd)

- **Interface when Diabetes is Detected** :

![Screenshot 2025-07-05 122922](https://github.com/user-attachments/assets/d2dab11d-0939-4d26-8eb6-a99188895073)

## 🤝 Contributing
- Contributions are welcome!
- If you'd like to improve the UI, add visualizations, or improve the model:

  - Fork the repo

  - Create a new branch

  - Submit a pull request 🚀

- If you find the project useful, feel free to ⭐ star the repository!

## 📄 License
- This project is licensed under the MIT License.

## 👨‍💻 Author
**Anshuman Dash**   
🎓 AIML Enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/ANSH5252) 

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/anshuman-dash-739793351/)