from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    # path('<int:pk>/', views.UserDetail.as_view(), name="users-detail"),
    path('', views.BookList.as_view(), name="books-list"),
]
