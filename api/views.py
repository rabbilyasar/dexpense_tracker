from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ExpenseSerializer
from tracker.models import Expense


@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List': '/expense-list',
        'Detail View': '/expense-detail/<str:pk>/',
        'Create': '/expense-create/',
        'Update': '/expense-update/<str:pk>',
        'Delete': '/expense-delete/<str:pk>'
    }

    return Response(api_urls)


@api_view(['GET'])
def expenseList(request):
    expenses = Expense.objects.all()
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def expenseDetail(request, pk):
    expense = Expense.objects.get(id=pk)
    serializer = ExpenseSerializer(expense, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def expenseCreate(request):
    serializer = ExpenseSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def expenseUpdate(request, pk):
    expense = Expense.objects.get(id=pk)
    serializer = ExpenseSerializer(instance=expense, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def expenseDelete(request, pk):
    expense = Expense.objects.get(id=pk)
    expense.delete()

    return Response('Item successfully deleted')
