from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', include('app1.urls')),   # Home page handled by app1
    path('app2/', include('app2.urls')),  # app2 routes
]
