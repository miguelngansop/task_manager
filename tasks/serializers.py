import datetime
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'completed', 'importance']
    
    # def validate_importance(self, value):
    #         if value not in ['Low', 'Medium', 'High']:
    #             raise serializers.ValidationError("L'importance doit être 'Low', 'Medium', ou 'High'")
    #         return value
            
    # def validate(self, data):
    #     if data.get('due_date') < datetime.now():
    #         raise serializers.ValidationError("La date d'échéance ne peut pas être dans le passé")
    #     return data