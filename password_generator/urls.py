from django.urls import path, include
from .views import home, password, login, about

urlpatterns = [
    path('', home, name='home'),
    path('generatedpassword/', password, name='password'),
    ## line 3 #path('generatedpassword/', password),
    path('login/', login, name='login'),
    path('about/', about, name='about'),
]
