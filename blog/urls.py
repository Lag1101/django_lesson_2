from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ArticleView.as_view(), name='article'),
    path('<int:pk>/new_comment', views.NewComment.as_view(), name='new_comment'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('signup/', views.SignUp.as_view(), name='signup'),
]
