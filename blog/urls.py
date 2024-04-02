from django.urls import path
from . import views

urlpatterns = [
    # 수정할 부분
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view())
]