# 🎓 Student Performance Prediction Using Machine Learning

## 📌 Project Overview

The Student Performance Prediction project uses Machine Learning techniques to predict students' average examination scores based on various factors such as gender, parental education, lunch type, race/ethnicity, and test preparation course.

The main objective is to analyze student data, identify performance patterns, and build predictive models that estimate students' academic performance.

## 🎯 Objectives

- Analyze student examination performance.
- Perform Exploratory Data Analysis (EDA).
- Identify factors associated with academic performance.
- Build Machine Learning regression models.
- Compare model performance using evaluation metrics.
- Develop an interactive web application using Streamlit.

## 📂 Dataset Information

**Dataset:** Students Performance in Exams

**Total Records:** 1,000 students

**Features:**
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

A new feature called `average_score` is created using the average of math, reading, and writing scores.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Google Colab

## 🔍 Project Workflow

1. Data Loading
2. Data Understanding
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Univariate Analysis
6. Bivariate Analysis
7. Feature Engineering
8. Feature Selection
9. Categorical Encoding
10. Train-Test Split
11. Machine Learning Model Building
12. Model Evaluation
13. Cross Validation
14. Model Comparison
15. Model Saving
16. Streamlit Web Application Development

## 🤖 Machine Learning Algorithms

The following regression algorithms are implemented:

1. Linear Regression
2. Decision Tree Regression
3. Random Forest Regression
4. K-Nearest Neighbors (KNN) Regression

## 📊 Model Evaluation Metrics

The models are evaluated using:

- **MAE:** Mean Absolute Error
- **MSE:** Mean Squared Error
- **RMSE:** Root Mean Squared Error
- **R² Score:** Coefficient of Determination

The best-performing model is selected based on RMSE.

## 🌐 Streamlit Web Application

An interactive web application is developed using Streamlit.

Users can enter student details, including:

- Gender
- Race/Ethnicity
- Parental Education
- Lunch Type
- Test Preparation Course

The trained Machine Learning model predicts the student's estimated average examination score.

## 📁 Project Structure

```text
Student-Performance-Prediction/
│
├── exams.csv
├── student_performance.py
├── app.py
├── student_performance_model.pkl
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Execution

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Streamlit Application

```bash
streamlit run app.py
```

### Step 4: Open the Application

Open the local URL displayed in your terminal:

```text
http://localhost:8501
```

## 💡 Key Learning Outcomes

- Understanding the complete Machine Learning workflow.
- Performing data analysis and visualization.
- Applying regression algorithms.
- Evaluating and comparing predictive models.
- Deploying a Machine Learning model using Streamlit.

## 🚀 Future Improvements

- Improve prediction accuracy through hyperparameter tuning.
- Include additional student performance-related features.
- Experiment with advanced regression algorithms.
- Deploy the application publicly.

## 👨‍💻 Author

**Nihal Noushad**

Aspiring Data Scientist | Python | SQL | Machine Learning | Power BI

---

⭐ If you find this project useful, feel free to explore the repository!
