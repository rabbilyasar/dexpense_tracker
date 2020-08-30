from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings


app_name = 'account'
urlpatterns = [
    path('register', views.registerPage, name="register"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutPage, name="logout"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
