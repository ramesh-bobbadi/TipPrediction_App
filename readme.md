# TipPrediction_App

A full-stack Machine Learning web application that predicts restaurant tip amounts based on user inputs using an **XGBoost** model. The application consists of a **React** frontend, a **Django REST Framework** backend, and a trained machine learning model integrated for real-time predictions.

---

## Features

- Predicts restaurant tip amounts using a trained XGBoost model.
- Responsive React user interface.
- REST API built with Django REST Framework.
- Real-time prediction using a pre-trained machine learning model.
- Input validation using Django serializers.
- Automatic encoding of categorical features before prediction.
- Clean separation between frontend, backend, and ML model.

---

## Tech Stack

### Frontend
- React
- Axios
- HTML
- CSS
- JavaScript

### Backend
- Django
- Django REST Framework
- Python

### Machine Learning
- XGBoost
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## Machine Learning Workflow

1. Collected and explored the dataset.
2. Performed data preprocessing.
3. Encoded categorical features.
4. Split the dataset into training and testing sets.
5. Trained an XGBoost regression model.
6. Evaluated model performance.
7. Saved the trained model using Joblib.
8. Integrated the trained model into the Django backend.

---

## How Prediction Works

1. The user enters:
   - Total Bill
   - Gender
   - Smoker
   - Day
   - Time

2. React sends the data to the Django REST API using Axios.

3. Django validates the request using `TipPredictionSerializer`.

4. Categorical values are encoded into numerical values.

5. The trained XGBoost model loads from disk.

6. The model predicts the restaurant tip.

7. Django returns the prediction as a JSON response.

8. React displays the predicted tip instantly.

---

## User Input Form

The frontend form is implemented in **Form.jsx**.

It collects the following inputs:

- Total Bill
- Sex
- Smoker
- Day
- Time

After the user submits the form:

- Axios sends a POST request to the Django API.
- The backend validates the input.
- The trained model generates a prediction.
- The predicted tip is returned to the frontend.
- React displays the prediction on the page.

---

## API Endpoint

The API is created using **Django REST Framework ViewSets** and a router.

### Endpoint

```
POST /tp_data/
```

### Request Body

```json
{
  "total_bill": 24.5,
  "sex": "Male",
  "smoker": "No",
  "day": "Sun",
  "time": "Dinner"
}
```

### Example Response

```json
{
  "id": 1,
  "total_bill": 24.5,
  "sex": "Male",
  "smoker": "No",
  "day": "Sun",
  "time": "Dinner",
  "predicted_tip": 3.82
}
```

---

## Project Structure

```
TipPrediction_App/
│
├── Backend/
│   ├── ml_app/
│   ├── models/
│   │   └── xgboost_model.pkl
│   ├── manage.py
│   └── requirements.txt
│
├── Frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── ML_Model/
│   ├── 01_ml.ipynb
│   └── dataset.csv
│
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/TipPrediction_App.git
cd TipPrediction_App
```

---

## Backend Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the Django server:

```bash
python manage.py runserver
```

Backend runs at:

```
http://127.0.0.1:8000/
```

---

## Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Frontend runs at:

```
http://localhost:5173/
```

---

## Running the Project

1. Start the Django backend.
2. Start the React frontend.
3. Open the frontend in your browser.
4. Enter the required input values.
5. Click the **Predict** button.
6. View the predicted restaurant tip instantly.

---

## Future Improvements

- User authentication
- Prediction history
- Charts and analytics dashboard
- Docker deployment
- Cloud deployment
- Model retraining pipeline
- Multiple regression model comparison

---

## Author

**Bobbadi Ramesh**

GitHub: https://github.com/manchalasudharshan

LinkedIn: https://linkedin.com/in/manchalasudharshan-b8bb42249
