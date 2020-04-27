


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
    path('register/', views.register), 
    path('login/', views.login), 
    path('success/', views.success), 

] 
