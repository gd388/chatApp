
from django.contrib import admin
from django.urls import path,include
from chatApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('chatApp.urls'))
]
