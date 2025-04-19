from django.shortcuts import render
import openpyxl


# Create your views here.
from rest_framework import viewsets
from .models import Task
from django.http import HttpResponse
from .serializers import TaskSerializer
from rest_framework.decorators import api_view


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer


@api_view(['GET'])
def export_tasks_to_excel(request):
    # Create workbook
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Tasks"

    # Headers
    ws.append(['Title', 'Description', 'Effort (days)', 'Due Date', 'Created At'])

    # Data
    tasks = Task.objects.all()
    for task in tasks:
        ws.append([
            task.title,
            task.description,
            task.effort,
            task.due_date.strftime('%Y-%m-%d'),
            task.created_at.strftime('%Y-%m-%d %H:%M'),
        ])

    # Return as Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=tasks.xlsx'
    wb.save(response)
    return response