
from django.urls import path
# from first_app.views import home          or
# from first_app import views               or
from . import views
urlpatterns = [
    path('', views.home),
]
