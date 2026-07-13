import joblib
from pathlib import Path
from django.conf import settings

MODEL_PATH = Path(settings.BASE_DIR).parent / 'ml_project' / 'xgb_model.pkl'
SEX_ENCODER_PATH = Path(settings.BASE_DIR).parent / 'ml_project' / 'le_sex.pkl'
DAY_ENCODER_PATH = Path(settings.BASE_DIR).parent / 'ml_project' / 'le_day.pkl'
SMOKER_ENCODER_PATH = Path(settings.BASE_DIR).parent / 'ml_project' / 'le_smoker.pkl'
TIME_ENCODER_PATH = Path(settings.BASE_DIR).parent / 'ml_project' / 'le_time.pkl'

model = joblib.load(MODEL_PATH)
le_sex = joblib.load(SEX_ENCODER_PATH)
le_day = joblib.load(DAY_ENCODER_PATH)
le_smoker = joblib.load(SMOKER_ENCODER_PATH)
le_time = joblib.load(TIME_ENCODER_PATH)

def en_code(data):
    return {
        'total_bill' : data['total_bill'],
        'sex' : le_sex.transform([data['sex']])[0],
        'smoker': le_smoker.transform([data['smoker']])[0],
        'day': le_day.transform([data['day']])[0],
        'time': le_time.transform([data['time']])[0],
    }