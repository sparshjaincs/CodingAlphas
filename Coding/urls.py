from django.urls import path
from . import views
urlpatterns = [
    path("",views.problems,name="coding"),
    path("practise/<var>/",views.inside,name="inside"),
]