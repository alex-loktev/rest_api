from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CarCreateView.as_view()),
    path('list/', CarListView.as_view()),
    path('detail/<int:pk>/', CarDetailView.as_view())
]