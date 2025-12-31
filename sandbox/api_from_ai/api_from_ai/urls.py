from django.contrib import admin
from django.urls import path, include
from .views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check),
    path('v1/', include('v1.urls')),  # Include v1 routes
]