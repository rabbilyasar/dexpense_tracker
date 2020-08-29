from django.contrib import admin
from django.urls import path, include

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),
    path('account/', include('account.urls')),
    path('api/', include('api.urls'))
]
