from django.urls import path
from .views import *

urlpatterns = [
    path('',HomePage),
    path('login/',LoginPage),
    path('registerUser/',Register),
    path('user/bookslot',Bookslot),
    path('user/<str:user>',User),
    path('lecturer/<str:lecturer>',Lecturer),
    path('useradmin/logout',logout),
    path('useradmin/addcourse',addcourse),
    path('useradmin/addtutor',addtutor),
    path('useradmin/removetutor',deletetutor),
    path('useradmin/<str:admin>',admin),
    path('validate',validate),
]
