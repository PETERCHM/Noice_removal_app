from django.urls import path
from . import views

urlpatterns = [
    path('process-form/', views.process_form, name='process_form'),
]
