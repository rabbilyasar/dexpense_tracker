from django.urls import path
from api import views

urlpatterns = [
    path('', views.apiOverview, name="api_overview"),
    path('expense-list/', views.expenseList, name="expense_list"),
    path('expense-detail/<str:pk>/', views.expenseDetail, name="expense_detail"),
]
