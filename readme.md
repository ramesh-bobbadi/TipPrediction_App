# Python ML models with Django

This is repository demostates how to develop and deploy machine learning models using Django framework. It includes examples of various ML models, their training, evaluation, and deployment as web applications.  

## 1. Create Python env

we will use python env to create the env

```bash
 # createe a virtual evnvironment 
 python -m venv .venv
 
 # activate the virtual environment for linux mac
 source .venv/bin/activate
 # for widows
 .venv\Scripts\activate
 ```
 ## 2. Install python libraries

 ```base
 # web development framwork
 pip install django
 # machine learing libraries
pip install number pandas matplotlib seaborn plotly scikit-learn sgboost
```
## 3. Train your machine learning model

1. Find the data
2. Preprocess the data
3. Train the model
4. Evaluate the model
5. Save the model
6. Create a Django view for your model

I have saved the model as `xgb_model.pkl` in the `models` directory.
You can see the procedure of Ml training a model in this and saving in this directory[jupyter notebook](./ml_project/01_ml.ipynb)

 
## 4. Create a Django project

```base
django-admin startprpject tip_prediction
cd tip_prediction
```

## 5 Create a Django app

```base
python manage.py startapp ml_app
```

## 6. Update settings.py

Add the new app to `INSTALLED_APP` list in `tip_prediction/settings.py`

## Create a form for user input
