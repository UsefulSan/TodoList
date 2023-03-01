from rest_framework.generics import CreateAPIView

from core.models import User
from core.serializers import UserCreateSerializer


class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


