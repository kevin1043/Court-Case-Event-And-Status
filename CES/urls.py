from django.urls import path
from CES import views
from .views import home


urlpatterns = [
    path('', views.home, name='home'),
]
