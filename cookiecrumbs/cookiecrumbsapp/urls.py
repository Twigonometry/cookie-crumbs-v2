from . import views
from django.urls import path

urlpatterns = [
    path('cookieCrumbs', views.cookieCrumbs, name='cookieCrumbs'),
    path('getTrail', views.getTrail, name='getTrail'),
    path('cookieTrail', views.cookieTrail, name='cookieTrail')
]