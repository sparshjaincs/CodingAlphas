from django.urls import path
from . import views
urlpatterns = [
    path("",views.jobs,name="jobs"),
    path('listing/',views.show_jobs,name="show_jobs"),
    path('companies/',views.companies,name="companies"),
    path('companies/<name>/',views.company_info,name="company_info"),
    path('current_hiring/',views.current_hiring,name="current"),
]