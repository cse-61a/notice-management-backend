from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import Student, CustomToken
from .serializers import StudentLoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
import secrets

class StudentLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = StudentLoginSerializer(data=request.data)
        if serializer.is_valid():
            student_id = serializer.validated_data['student_id']
            student = Student.objects.get(student_id=student_id)

            # Generate or retrieve a token for the student
            token, created = CustomToken.objects.get_or_create(
                student=student,
                defaults={'token': secrets.token_hex(16)}
            )

            return Response({
                "token": token.token,
                "student_name": student.name,
                "message": "Login successful!"
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def post(self, request):
        # Extract the token from the Authorization header
        token = request.headers.get('Authorization')

        if not token:
            return Response({"detail": "Token not provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Extract the token part after 'Bearer'
            token = token.split(' ')[1]
        except IndexError:
            return Response({"detail": "Invalid token format. Token should be in the form 'Bearer <token>'."},
                             status=status.HTTP_400_BAD_REQUEST)

        try:
            # Delete the token from the CustomToken model
            custom_token = CustomToken.objects.get(token=token)
            custom_token.delete()

            return Response({"message": "Logout successful. Token deleted."}, status=status.HTTP_200_OK)

        except CustomToken.DoesNotExist:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)