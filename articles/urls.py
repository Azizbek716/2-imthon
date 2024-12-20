from django.urls import path
from . import views



app_name='articles'

urlpatterns = [
    path('create/', views.create_articles, name='create'),
    path('category/<str:category>', views.articles_by_category, name='category'),
    path('detail/<int:pk>', views.articles_detail, name='detail')
]

