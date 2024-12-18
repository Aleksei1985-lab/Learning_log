"""Определяет схемы URL для learning_logs."""
from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # вывод всех тем
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>\d+', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>\d+', views.new_entry, name='new_entry'),
    # Страница для редактирования записи 
    path('edit_entry/<int:entry_id>\d+', views.edit_entry, name='edit_entry'),
]