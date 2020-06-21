from django.urls import path
from . import views

urlpatterns = [
    path('<int:policy_id>', views.index, name='policy'),
]
