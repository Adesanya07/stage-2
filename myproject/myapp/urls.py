from django.urls import path
from .views import getPerson, addPerson, editPerson, deletePerson

urlpatterns = [
    path('person/<str:name>/', getPerson),
    path('add/', addPerson),
    path('edit/<str:name>/', editPerson),
    path('delete/<str:name>/', deletePerson),
]