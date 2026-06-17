# 🌸 Iris Flower Species Classifier

A machine learning project that classifies Iris flowers into three species using Logistic Regression, built with Python and scikit-learn.

---

## 📌 Overview

This project trains a classification model on the classic Iris dataset to predict the species of an Iris flower based on its physical measurements. The trained model is saved as `model.pkl` for reuse without retraining.

**Target Classes:**
- `0` → Iris-setosa
- `1` → Iris-versicolor
- `2` → Iris-virginica

---

## 📁 Project Structure

~~~
Iris_Model/
├── Data/
│   └── Iris.csv            # Dataset
├── Iris_Model.ipynb        # Jupyter Notebook (training pipeline)
├── model.pkl               # Saved trained model
└── README.md
~~~

---

## 🔧 Technologies Used

| Library       | Purpose                          |
|---------------|----------------------------------|
| pandas        | Data loading and manipulation    |
| numpy         | Numerical operations             |
| scikit-learn  | Model training and evaluation    |
| pickle        | Saving and loading the model     |

---

## ⚙️ Workflow

1. **Load Dataset** — Read `Iris.csv` using pandas
2. **Encode Labels** — Convert species names to numeric values using `LabelEncoder`
3. **Prepare Features** — Drop `Id` and original `Species` columns; use sepal/petal measurements as input features
4. **Split Data** — 80% training / 20% testing using `train_test_split` (`random_state=42`)
5. **Train Model** — Fit a `LogisticRegression` model (`max_iter=1000`)
6. **Evaluate** — Measure accuracy using `accuracy_score` and compare actual vs predicted values
7. **Save Model** — Serialize the trained model to `model.pkl` using `pickle`

---

## 📊 Dataset Features

| Feature          | Description                  |
|------------------|------------------------------|
| SepalLengthCm    | Length of the sepal (cm)     |
| SepalWidthCm     | Width of the sepal (cm)      |
| PetalLengthCm    | Length of the petal (cm)     |
| PetalWidthCm     | Width of the petal (cm)      |
| Species          | Target label (flower species)|

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/iris-model.git
cd iris-model
```

### 2. Install dependencies
```bash
pip install pandas numpy scikit-learn jupyter
```

### 3. Run the notebook
```bash
jupyter notebook Iris_Model.ipynb
```

### 4. Load the saved model (optional)
```python
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Example prediction
sample = [[5.1, 3.5, 1.4, 0.2]]  # SepalLength, SepalWidth, PetalLength, PetalWidth
prediction = model.predict(sample)
print(prediction)  # Output: [0] → Iris-setosa
```

---

## ✅ Results

The model was successfully trained and evaluated. Actual vs predicted values were compared side by side — all predictions matched the expected labels, confirming the model is working correctly.

---

## 📝 Notes

- Ensure `Iris.csv` is placed inside the `Data/` folder before running the notebook.
- The saved `model.pkl` can be loaded and used directly without retraining.
- This project was developed as part of the **DecodeLab Internship** (Project 2).