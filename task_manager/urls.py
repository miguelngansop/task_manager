
from django.contrib import admin
from django.urls import path
from tasks.views import TaskDetailAPIView, TaskListCreateAPIView
from tasks.views import signup, login, test_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
        title="Task Management API",
        default_version='v1',
        description="This API is built using Django Rest Framework as part of a test provided by Doctustech. It provides endpoints for managing tasks, including creating, retrieving, updating, and deleting tasks. The API is designed to be RESTful and follows standard HTTP methods and status codes for interaction. It offers authentication and authorization mechanisms to ensure secure access to the endpoints. Swagger UI is integrated to provide an interactive documentation for developers.",
        contact=openapi.Contact(email="regisarmel.ngansop@gmail.com"),
    ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('api/auth/signup/', signup, name='signup'),
    path('api/auth/login/', login, name='login'),
    path('api/auth/test_token/', test_token, name='test_token'),
]
