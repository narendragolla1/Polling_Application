from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('question/<slug>',views.Question.as_view(),name='question'  )
]
