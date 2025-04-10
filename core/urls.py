from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='Homepage'),
    path('question/<int:question_id>/',views.question_detail_view, name='question_detail'),
    path('answer/<int:answer_id>/like/', views.like_answer_view, name='like_answer'),
]
