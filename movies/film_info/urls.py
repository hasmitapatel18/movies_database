from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.homepage, name='homepage'),
    path(r'register/', views.register, name='register'),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path('reviewpage/<int:review_id>', views.reviewpage, name='reviewpage'),
]
