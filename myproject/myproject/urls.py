from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home),
    path('index/', home),    # Maps the /home/ URL to the home view
    path('about/', about), # Maps the /about/ URL to the about view
    path('contact/', contact),
    path('mytemp/', mytemp),
    path('emp/', include('emp.urls'))

]