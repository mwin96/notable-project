from django.urls import path
from . import views
from info.views import *

urlpatterns = [
    path('patients/', views.InfoListCreate.as_view()),
    path('',IndexView.as_view()),
    path('physicians/', views.PhysiciansListCreate.as_view()),
]