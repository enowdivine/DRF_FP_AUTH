from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User
from .serializer import UserSerializer


@api_view(["GET"])
def users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(["POST"])
def login(request):
    try:
        user = User.objects.get(email=request.data["email"])
    except:
        return Response(
            {"error": "Authentication Failed"}, status=status.HTTP_401_UNAUTHORIZED
        )
    serializered_user = UserSerializer(user)
    if serializered_user.data["password"] == request.data["password"]:
        return Response(
            {"message": "Login successful", "data": serializered_user.data},
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {"error": "Authentication Failed"}, status=status.HTTP_401_UNAUTHORIZED
        )
