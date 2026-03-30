from django.contrib import admin
from django.urls import path, include
from crud.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('notes.urls')),
    path('testjwt/', include('testjwt.urls')),
    path('', home),  # Root URL
]