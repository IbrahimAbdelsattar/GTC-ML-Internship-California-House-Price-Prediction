# 🏡 California House Price Prediction  

## 📌 Project Overview  
This project focuses on predicting **median house values in California districts** using **Machine Learning (ML) and Deep Learning (DNN)** models.  
The dataset contains demographic, geographic, and economic features that influence housing prices.  
By analyzing and modeling these features, the project provides accurate predictions that can support **real estate analysis, urban planning, and investment decisions**.  

---

## 🔍 Why This Project Matters  
- 🏠 **Real Estate Investors** → Helps them evaluate potential investment opportunities.  
- 📊 **Policy Makers & Urban Planners** → Gain insights into factors affecting housing prices.  
- 👨‍👩‍👧 **Home Buyers & Sellers** → Get a fair estimate of property prices in different locations.  
- 🧑‍💻 **Data Science Learners** → Understand how to handle **EDA, preprocessing, outlier handling, feature engineering, modeling, and deployment**.  

Accurate house price prediction is **critical** for making informed decisions in the **housing market**, which directly impacts **economic growth and individual financial planning**.  

---

## ⚙️ Steps of the Project  

1. **Data Collection & Understanding**  
   - Used the **California Housing Dataset**.  
   - Explored key features like `longitude`, `latitude`, `median_income`, `total_rooms`, and `ocean_proximity`.  

2. **Data Preprocessing**  
   - Handled **missing values** and **outliers**.  
   - Applied **encoding techniques** (Label Encoding / One-Hot Encoding).  
   - Scaled numerical features using **StandardScaler**.  

3. **Exploratory Data Analysis (EDA)**  
   - **Univariate, Bivariate, and Multivariate Analysis** with interactive charts.  
   - Discovered relationships between features and `median_house_value`.  

4. **Modeling**  
   - Implemented multiple ML models: **Linear Regression, Ridge, Lasso, Decision Tree, Random Forest, Gradient Boosting**.  
   - Built a **Deep Neural Network (DNN)**.  
   - Tuned hyperparameters for better accuracy.  
   - Achieved best performance with **LightGBM and Stacking Regressor (R² = 0.85)**.  

5. **Evaluation**  
   - Used metrics: **MAE, MSE, RMSE, and R² Score**.  
   - Compared models’ performance in a summary table.  

6. **Deployment**  
   - Developed an **interactive Streamlit web app**.  
   - Users can input features and get **predicted house prices in USD** instantly.  

---

## 🚀 Key Results  

| Model                | MAE   | MSE   | RMSE  | R²   |
|----------------------|-------|-------|-------|------|
| Linear Regression    | 0.44  | 0.36  | 0.60  | 0.63 |
| Decision Tree        | 0.38  | 0.35  | 0.59  | 0.64 |
| Random Forest        | 0.28  | 0.18  | 0.43  | 0.82 |
| Gradient Boosting    | 0.33  | 0.24  | 0.49  | 0.76 |
| Deep Neural Network  | 0.30  | 0.20  | 0.45  | 0.80 |
| **LightGBM**         | 0.25  | 0.15  | 0.38  | 0.85 |
| **Stacking Regressor** | 0.25  | 0.15  | 0.38  | 0.85 |

✅ Best models: **LightGBM** and **Stacking Regressor** with **R² = 0.85**.  

---

## 👥 Who Can Use This Project?  
- **Real Estate Companies** → Price recommendation systems.  
- **Government Agencies** → Urban development and planning.  
- **Banks & Loan Providers** → Risk assessment for mortgages.  
- **Data Science Enthusiasts** → End-to-end ML/DL project reference.  

---

## 🛠️ Tech Stack  
- **Languages**: Python  
- **Libraries**: Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn, Plotly, TensorFlow/Keras, LightGBM  
- **Deployment**: Streamlit  

---

## 🌟 Conclusion  
This project demonstrates how **machine learning and deep learning** can effectively predict real-world housing prices.  
By combining data preprocessing, visualization, feature engineering, and advanced modeling, we achieved strong results that can serve as a foundation for **real estate predictive analytics applications**.  

---
