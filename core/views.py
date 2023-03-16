from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, \
    UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import User
from core.serializers import UserCreateSerializer, UserProfileRetrieveSerializer, \
    UpdatePasswordSerializer


class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class LoginView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'username': username, 'password': password})
        else:
            raise AuthenticationFailed('Wrong username or password')


class UserProfileView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileRetrieveSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        return queryset.get(pk=self.request.user.pk)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response()


class UpdatePasswordView(UpdateAPIView):
    serializer_class = UpdatePasswordSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
