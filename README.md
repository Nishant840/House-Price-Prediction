# House Price Prediction using Linear Regression

## 📌 Project Overview
This project aims to predict house prices in Bengaluru using **Linear Regression** and **regularized regression models** like **Lasso and Ridge Regression**. The dataset is sourced from **Kaggle** and contains various features such as location, size, total square feet, number of bathrooms, and price.

## 📂 Repository Structure
```
├── data/                 # Raw and processed datasets
├── notebooks/            # Jupyter notebooks for EDA and model training
├── src/                  # Python scripts for data preprocessing and model training
├── models/               # Saved machine learning models
├── requirements.txt      # Dependencies for the project
└── README.md             # Project documentation
```

## 🛠️ Steps Followed
1. **Data Cleaning & Preprocessing**
   - Removed unnecessary columns (`area_type`, `society`, etc.)
   - Handled missing values and outliers
   - Standardized `price_per_sqft` values by filtering within [mean ± std_dev]
   - Encoded categorical variables using **One-Hot Encoding**

2. **Exploratory Data Analysis (EDA)**
   - Analyzed distributions using **Seaborn**
   - Visualized the relationship between price and features
   - Handled locations with very low frequency by grouping them into an "Other" category

3. **Feature Engineering**
   - Created a new `BHK` feature from the `size` column
   - Ensured that the `bathrooms` count did not exceed `BHK + 2`

4. **Model Training & Evaluation**
   - Used **Linear Regression, Lasso, and Ridge Regression**
   - Evaluated models using **R² Score**:
     - **Linear Regression**: `~0.80`
     - **Lasso Regression**: `~0.79`
     - **Ridge Regression**: `~0.80`

5. **Performance Improvement**
   - Tried feature selection to remove less relevant features
   - Regularized the model to prevent overfitting
   - Tested different hyperparameters for better performance

## 📊 Results & Insights
- The model achieves **~80% accuracy**, meaning it explains 80% of the variance in house prices.
- Lasso Regression slightly reduced R², indicating some features might not be highly relevant.
- Ridge Regression performed almost the same as Linear Regression, suggesting minimal multicollinearity issues.

## 🚀 How to Run the Project
### 1️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 2️⃣ Run the Jupyter Notebook
```sh
jupyter notebook
```

### 3️⃣ Execute the Python Script
```sh
python src/train_model.py
```

## 📜 License
This project is open-source and available under the **MIT License**.

