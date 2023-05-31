from django.urls import path
from app import views
urlpatterns=[
    path('login/',views.login.as_view()),
    path('logout/',views.logout.as_view()),
]