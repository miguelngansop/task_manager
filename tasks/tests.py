

from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from .views import signup, login, test_token, TaskListCreateAPIView, TaskDetailAPIView
from .models import Task
from tasks.constants import Importance


class TaskTests(APITestCase):
    TEST_USERNAME = 'testuser'
    TEST_USER_EMAIL = 'testuser@test.com'
    TEST_PASSWORD = 'testpassword'
    TEST_TASK_TITLE = 'Test Task'
    TEST_TASK_DESCRIPTION = 'This is a test task'
    TEST_TASK_DUE_DATE = '2024-04-15T12:00:00Z'

    def setUp(self):
        self.user = User.objects.create_user(username=self.TEST_USERNAME, password=self.TEST_PASSWORD, email=self.TEST_USER_EMAIL)
        self.factory = APIRequestFactory()

    def test_signup(self):
        request_data = {'username': self.TEST_USERNAME+'new', 'password': self.TEST_PASSWORD, 'email': 'x'+self.TEST_USER_EMAIL}
        response = signup(self.factory.post('/signup/', request_data))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        request_data = {'email': self.user.email, 'password': self.TEST_PASSWORD}
        response = login(self.factory.post('/login/', request_data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_test_token(self):
        request = self.factory.get('/test_token/')
        request.user = self.user
        response = test_token(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        request_data = {'title': self.TEST_TASK_TITLE, 'description': self.TEST_TASK_DESCRIPTION, 'due_date': self.TEST_TASK_DUE_DATE, 'created_by':self.user.id, 'importance': Importance.HIGH.value}
        request = self.factory.post('/tasks/', request_data)
        request.user = self.user
        response = TaskListCreateAPIView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['importance'], Importance.HIGH.value)

    def test_get_task_list(self):
        request = self.factory.get('/tasks/')
        request.user = self.user
        response = TaskListCreateAPIView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_task_detail(self):
        task = Task.objects.create(title=self.TEST_TASK_TITLE, description=self.TEST_TASK_DESCRIPTION, due_date=self.TEST_TASK_DUE_DATE, created_by=self.user)
        request = self.factory.get(f'/tasks/{task.id}/')
        request.user = self.user
        response = TaskDetailAPIView.as_view()(request, pk=task.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.TEST_TASK_TITLE)

    def test_update_task(self):
        task = Task.objects.create(title=self.TEST_TASK_TITLE, description=self.TEST_TASK_DESCRIPTION, due_date=self.TEST_TASK_DUE_DATE, created_by=self.user)
        updated_title = 'Updated Task'
        request_data = {'title': updated_title}
        request = self.factory.patch(f'/tasks/{task.id}/', request_data)
        request.user = self.user
        response = TaskDetailAPIView.as_view()(request, pk=task.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=task.id).title, updated_title)

    def test_delete_task(self):
        task = Task.objects.create(title=self.TEST_TASK_TITLE, description=self.TEST_TASK_DESCRIPTION, due_date=self.TEST_TASK_DUE_DATE, created_by=self.user)
        request = self.factory.delete(f'/tasks/{task.id}/')
        request.user = self.user
        response = TaskDetailAPIView.as_view()(request, pk=task.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
