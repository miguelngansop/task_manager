import logging
from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import render, redirect

@swagger_auto_schema(security=[{"TokenAuth": []}])
class TaskListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint to list and create tasks.

    Permissions:
    - User must be authenticated to access this endpoint.

    Attributes:
    - queryset: Queryset for retrieving tasks.
    - serializer_class: Serializer class for tasks.
    - permission_classes: List of permission classes required to access this endpoint.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
    operation_summary="Get user tasks",
    operation_description="This endpoint allows authenticated users to get the list of their tasks.",
    responses={200: "List of tasks"})
    def get_queryset(self):
        """
        Get the queryset of tasks for the authenticated user.
        """
        return Task.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        """
        Perform creation of a new task.

        Parameters:
        - serializer: Serializer instance for the task.

        Side Effects:
        - Sets the 'created_by' field of the task to the current authenticated user.
        """
        serializer.save(created_by=self.request.user)
        try:
            # Attempt to serialize the incoming data
            serializer = self.serializer_class(data=self.request.data)
            # Check if the serializer data is valid
            if serializer.is_valid():
                # Save the task with the authenticated user as the creator
                serializer.save(created_by=self.request.user)
                # Return a success response with the serialized data
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                # Return a bad request response with serializer errors if data is invalid
                Logger.error(f"An error occurred while creating the task: {serializer.errors}", exc_info=True)
                print('error: ', serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Log the exception along with its traceback
            Logger.error(f"An error occurred while creating the task: {e}", exc_info=True)
            # Return an appropriate error response
            return Response({"detail": "An error occurred while creating the task."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Configure the logger
Logger = logging.getLogger(__name__)

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, and delete a task.

    Permissions:
    - User must be authenticated to access this endpoint.

    Attributes:
    - queryset: Queryset for retrieving tasks.
    - serializer_class: Serializer class for tasks.
    - permission_classes: List of permission classes required to access this endpoint.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['POST'])
def signup(request):
    """
    API endpoint to register a new user.

    Parameters:
    - email: The email address of the new user.
    - username: The desired username for the new user.
    - password: The password for the new user.

    Returns:
    - HTTP 201 Created on successful registration.
    - HTTP 400 Bad Request if email, username, or password is missing, or if email is already taken.
    """
    # Retrieve email, username, and password from request data
    email = request.data.get('email')
    username = request.data.get('username')
    password = request.data.get('password')

    # Check if email, username, and password are provided
    if not email or not username or not password:
        # Return error response if email, username, or password is missing
        return Response("Email, username, and password are required", status=status.HTTP_400_BAD_REQUEST)

    try:
        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            # Return error response if email is already taken
            return Response("Email is already taken", status=status.HTTP_400_BAD_REQUEST)

        # Create a new user object
        user = User.objects.create(email=email, username=username)
        # Hash the password and set it for the user
        user.set_password(password)
        # Save the user object
        user.save()
        # Generate authentication token for the user
        token, _ = Token.objects.get_or_create(user=user)
        # Return success response with authentication token, username, and email
        return Response({'token': token.key, 'username': user.username, 'email': user.email}, status=status.HTTP_201_CREATED)
    except Exception as e:
        # Return error response for any other exceptions
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['POST'])
def login(request):
    """
    API endpoint to authenticate a user.

    Parameters:
    - email: The email address of the user.
    - password: The password of the user.

    Returns:
    - HTTP 200 OK with authentication token, username, and email on successful authentication.
    - HTTP 401 Unauthorized if authentication fails.
    """
    # Retrieve email and password from request data
    email = request.data.get('email')
    password = request.data.get('password')

    # Authenticate user using provided credentials
    user = authenticate(email=email, password=password)

    # Check if authentication is successful
    if user is not None:
        # Generate authentication token for the user
        token, _ = Token.objects.get_or_create(user=user)
        # Return success response with authentication token, username, and email
        return Response({'token': token.key, 'username': user.username, 'email': user.email}, status=status.HTTP_200_OK)
    else:
        # Return error response if authentication fails
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

#@swagger_auto_schema(exclude=True)
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    """
    API endpoint to test the validity of the authentication token.

    Returns:
    - HTTP 200 OK if the token is valid.
    - HTTP 401 Unauthorized if the token is invalid.
    """
    return Response("passed!")
