from django.urls import path
from .views import *

urlpatterns = [
   path('',home),
   path('blog/<slug:url>', post),
   path('category/<slug:url>', category),
   path('about/',about),
]

