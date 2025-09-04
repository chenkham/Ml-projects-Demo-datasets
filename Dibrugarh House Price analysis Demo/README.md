
# 🏠 Dibrugarh House Price Predictor

A machine learning project that predicts house prices in Dibrugarh using features like area, locality, building type, and more.

---

## 📌 Features

- Predicts house prices using a trained ML model
- Complete preprocessing pipeline: imputation, scaling, encoding
- Trained model saved using `joblib`
- Interactive terminal script for live predictions

---

## 📁 Project Structure

```
.
├── Dibrugarh_house.ipynb       # Jupyter Notebook (training pipeline)
├── predict_house.py            # Script for user input prediction
├── Dragon.joblib               # Saved trained model (joblib)
├── dib_house_prices.csv        # Raw dataset
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🚀 How to Run

### 1. Install requirements

```bash
pip install -r requirements.txt
```

### 2. Run the prediction script

```bash
python predict_house.py
```

You’ll be prompted to enter house features. The model will predict the house price.

---

## 🧠 Model Details

- Algorithm: Linear Regression (can be replaced by RandomForest, etc.)
- Preprocessing: `SimpleImputer`, `StandardScaler`, `OneHotEncoder`
- Label transformed using `np.log1p()`
- Final Log RMSE: `0.108` (≈ 11% error)

---

## ✅ Example Output

```
Enter the area in sqft: 1500
Enter the number of bedrooms: 3
...
🏠 Predicted House Price: ₹9,87,123.45
```

---

## 🙌 Author

**Chenkham Chowlu**  
BCA Student, Dibrugarh University  
GitHub: [github.com/chenkham](https://github.com/chenkham)


😊i didn't have time to write an README file so, I ask an AI model
to make it for me. we should not waste time on small things...

and I haven't used matplotlib because i want an quick model and my dataset was downloaded from chatgpt.
but you must use it to analyse the data efficiently.