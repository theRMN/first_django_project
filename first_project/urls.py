from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls'), name='home'),
    path('', include('app.urls'), name='time'),
    path('', include('app.urls'), name='workdir'),
    path('admin/', admin.site.urls),
]
