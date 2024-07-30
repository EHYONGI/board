from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.detail, name="detail") # posts(articles)/ 필요 X -> 중복된 거 빼서 !
]