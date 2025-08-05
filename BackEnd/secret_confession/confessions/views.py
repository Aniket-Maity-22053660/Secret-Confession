from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from .models import User, Confession, Reaction
from .serializers import UserSerializer, ConfessionSerializer, ReactionSerializer

# User Registration
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User(username=username, email=email, password=password)
        user.save()
        return Response({"message": "User registered successfully", "user_id": user.id})

# User Login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                return Response({"message": "Login successful", "user_id": user.id})
            else:
                return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

# Confessions API
class ConfessionViewSet(viewsets.ModelViewSet):
    queryset = Confession.objects.all().order_by('-created_at')
    serializer_class = ConfessionSerializer

# Reactions API
class ReactionViewSet(viewsets.ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
