from . models import Student
from rest_framework import serializers

class StudentLoginSerializer(serializers.Serializer):
    student_id = serializers.CharField(max_length=20)

    def validate_student_id(self, value):
        if not Student.objects.filter(student_id=value).exists():
            raise serializers.ValidationError("Invalid Student ID. Access denied.")
        return value