from django.shortcuts import render
import openpyxl


# Create your views here.
from rest_framework import viewsets
from .models import Task
from django.http import HttpResponse
from .serializers import TaskSerializer
from rest_framework.decorators import api_view


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('userId')
        if user_id:
            return Task.objects.filter(user_id=user_id).order_by('-created_at')
        return Task.objects.none()

    def perform_create(self, serializer):
        user_id = self.request.data.get('userId')
        serializer.save(user_id=user_id)

    def get_queryset(self):
        user_id = self.request.query_params.get('userId')
        if user_id:
            return Task.objects.filter(user_id=user_id).order_by('-created_at')
        return Task.objects.none()

    def perform_destroy(self, instance):
        user_id = self.request.query_params.get('userId')
        if instance.user_id != user_id:
            raise PermissionDenied("You can only delete your own tasks.")
        instance.delete()


@api_view(['GET'])
def export_tasks_to_excel(request):
    # Create workbook
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Tasks"

   
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