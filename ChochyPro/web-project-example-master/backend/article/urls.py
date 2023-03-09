from django.urls import path
from .views import ArticleView, OneAuthorView

app_name = "articles"
#app_name = "author"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('author/<int:pk>', OneAuthorView.as_view()),
]