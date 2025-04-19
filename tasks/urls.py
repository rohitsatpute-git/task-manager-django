from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, export_tasks_to_excel

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns += [
    path('export/excel/', export_tasks_to_excel, name='export-tasks-excel'),
]
