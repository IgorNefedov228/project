from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index ),
    path('page', views.page),
    path('pages', views.pages),
    path('pagess', views.pagess),
    path('pagesss', views.pagesss),
    path('page1', views.page1),
    path('pageo', views.pageo),
    path('pagep', views.pagep),
    path('pagepp', views.pagepp),
    path('sector', views.sector),
    

]
