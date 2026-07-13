from pathlib import Path
import numpy as np
from .ml_utils import model,en_code
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import joblib
from rest_framework import status, viewsets,permissions
from rest_framework.response import Response
from .models import TipPrediction   
from .serializers import TipPredictionSerializer

class TipPredictionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = TipPrediction.objects.all()
    serializer_class = TipPredictionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        encoded = en_code(serializer.validated_data)
        features = np.array([[
            encoded['total_bill'],
            encoded['sex'],
            encoded['smoker'],
            encoded['day'],
            encoded['time'],
        ]])
        prediction = model.predict(features)

        response_data = serializer.data
        response_data['predicted_tip'] = float(prediction[0])
        return Response(response_data, status=status.HTTP_201_CREATED)
 
def Home(request):
    return render(request,"Home.html")

def Tip_Prediction(request):
    return render(request,'Tip_Prediction.html')

def model_res(request):
    model_path = Path(settings.BASE_DIR).parent / 'ml_project' / 'xgb_model.pkl'
    model = joblib.load(model_path)  # Load the trained model
    input_data = [[ 4, 3, 0, 1, 0,]]  
    # Example input data; replace with actual input
    prediction = model.predict(input_data)
    return render(request, 'model.html',{'prediction':prediction[0]})

    