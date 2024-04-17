from django.db import models
from django.contrib.auth.models import User

from tasks.constants import ErrorMessage
from tasks.constants import Importance


class Task(models.Model):
    

    # Task fields
    title = models.CharField(max_length=200, error_messages={'blank': ErrorMessage.REQUIRED_FIELD, 'max_length': ErrorMessage.INVALID_TITLE})
    description = models.TextField(blank=True, error_messages={'max_length': ErrorMessage.INVALID_DESCRIPTION})
    due_date = models.DateTimeField(error_messages={'invalid': ErrorMessage.INVALID_DUE_DATE})
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, error_messages={'invalid': ErrorMessage.INVALID_CREATED_BY})
    importance = models.CharField(
        max_length=10, choices=[(choice.value, choice.name) for choice in Importance],
        default=Importance.LOW.value, #low
        error_messages={'invalid_choice': ErrorMessage.INVALID_IMPORTANCE})

    def __str__(self):
        return self.title

