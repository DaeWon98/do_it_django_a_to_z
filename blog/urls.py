from django.urls import path
from . import views

urlpatterns = [
    # 수정할 부분
    path('', views.index)
]