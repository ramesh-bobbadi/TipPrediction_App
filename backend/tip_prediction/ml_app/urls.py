from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import TipPredictionViewSet

router = DefaultRouter()

router.register('tp_data',TipPredictionViewSet,basename='tp_data')
urlpatterns = [
    path('home/',views.Home),
    path('tipprediction/',views.Tip_Prediction),
    path('model/',views.model_res)
] + router.urls

