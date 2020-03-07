from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new_article/', views.NewArticle.as_view(), name='new_article'),
    path('<int:pk>/', views.ArticleView.as_view(), name='article'),
    path('<int:pk>/new_comment', views.NewComment.as_view(), name='new_comment'),
    # path('<int:pk>/<int:comment_key>/new_comment', views.NewComment.as_view(), name='new_sub_comment'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('signup/', views.SignUp.as_view(), name='signup'),

    path('person/<int:pk>/', views.PersonView.as_view(), name='person'),
    # path('person/<int:pk>/edit', views.PersonEditView.as_view(), name='person_edit'),
]
