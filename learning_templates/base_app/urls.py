from django.urls import path, include
from base_app import views

app_name = "base_app"
urlpatterns = [
    path('relative/', views.relative, name = "relative"),
    path('other/', views.other, name = "other"),

]
