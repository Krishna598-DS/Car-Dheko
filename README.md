# Car-Dheko
Used Car Price Prediction
🚗 Used Car Price Prediction - CarDekho (ML + Streamlit App)
🧾 Problem Statement
Imagine you are working as a data scientist at CarDekho. Your objective is to enhance customer experience and streamline the pricing process by leveraging machine learning. Your mission is to build a user-friendly web application using Streamlit that predicts the prices of used cars based on their features.

The tool should be interactive and accurate, allowing both customers and sales representatives to input car details and instantly receive a price prediction.

🎯 Project Objective
Develop a machine learning model to predict used car prices.
Build a Streamlit-based web app for real-time predictions.
Deploy the model in a user-friendly interface to assist decision-making.

🗂️ Project Scope
The project uses historical used car data from multiple cities.
Dataset includes car make, model, year, fuel type, transmission, and other attributes.
The final product is a deployed ML model integrated with a Streamlit application.

🔍 Approach
1️⃣ Data Processing
Import and Concatenate:
Load multiple city datasets.
Convert unstructured data to structured format.
Add a ‘City’ column to each dataset.
Merge all city datasets into a single dataframe.

Handle Missing Values:
For numeric columns: Use mean/median/mode.
For categorical columns: Use mode or assign "Unknown".

Standardize Data Formats:
Convert columns like "70 kms" to integers by removing units.
Ensure correct data types for all features.

Encoding Categorical Variables:
Apply one-hot encoding for nominal features.
Apply label/ordinal encoding for ordered categories.
Normalize Numerical Features (if needed):
Use Min-Max Scaling or Standard Scaling.
Remove Outliers:
Use IQR or Z-score methods to identify and treat outliers.

2️⃣ Exploratory Data Analysis (EDA)
Descriptive Statistics:
Summary stats: Mean, median, standard deviation, etc.
Data Visualization:
Histograms, scatter plots, boxplots, and heatmaps to understand patterns.
Feature Selection:
Use correlation matrices, feature importance scores, and domain knowledge.

3️⃣ Model Development
Train-Test Split:
Typically use an 80-20 or 70-30 ratio.

Model Selection:
Algorithms:
Linear Regression
Decision Tree
Random Forest
Gradient Boosting (XGBoost, LightGBM)

Model Training:
Use cross-validation for better generalization.
Hyperparameter Tuning:
Use GridSearchCV or RandomizedSearchCV for optimization.

4️⃣ Model Evaluation
Metrics:
Mean Absolute Error (MAE)
Mean Squared Error (MSE)
R² Score
Model Comparison:
Evaluate all models and select the one with best generalization performance.

5️⃣ Optimization
Feature Engineering:
Create new relevant features using domain knowledge.
Regularization:
Use Lasso (L1) or Ridge (L2) to prevent overfitting in linear models.

🌐 Streamlit Web App
Users can input car details through an interactive form.
The app displays the predicted price instantly.
Designed for ease of use by both customers and CarDekho sales teams.

![Application](https://github.com/user-attachments/assets/cc091107-0fa2-4228-b328-db99baddb1d2)
