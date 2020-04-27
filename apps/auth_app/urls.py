


''' 
================================================================================ 
================================================================================ 
                           APP-LEVEL URLS.PY: auth_app 
================================================================================ 
================================================================================ 
''' 



from django.urls import path 
from django.conf.urls import url 
from . import views 

urlpatterns = [ 
    path('', views.index), 
    path('register/', views.registerUser), 
    path('login/', views.loginUser), 
    path('success/', views.success), 
    path('userFormRoute/', views.userFormRoute), 

] 
