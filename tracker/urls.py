from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings


app_name = 'tracker'
urlpatterns = [
    path('', views.home, name='home'),
    path('approved_expenses', views.approvedExpenses, name="approved_expense"),
    path('create_expense', views.createExpense, name='create_expense'),
    path('update_expense/<str:pk>', views.updateExpense, name='update_expense'),
    path('delete_expense/<str:pk>', views.deleteExpense, name='delete_expense'),
    path('change_status/<str:pk>', views.changeStatus, name='change_status')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
