from django.urls import path
from api import views

urlpatterns = [
    path('', views.apiOverview, name="api_overview"),
    path('expense-list/', views.expenseList, name="expense_list"),
    path('expense-detail/<str:pk>/', views.expenseDetail, name="expense_detail"),
    path('expense-create/', views.expenseCreate, name="expense_detail"),
    path('expense-update/<str:pk>/', views.expenseUpdate, name="expense_update"),
    path('expense-delete/<str:pk>/', views.expenseDelete, name="expense_delete"),

]
