from django.urls import path
from . import views

urlpatterns = [
    # 수정할 부분
    path('<int:pk>/', views.single_post_page),
    path('', views.PostList.as_view())
]