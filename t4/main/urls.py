from django.urls import path
from .views import index, by_rubric, BboardCreateView, about
      
urlpatterns = [
    path('add/', BboardCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('about/', about, name='about')
]