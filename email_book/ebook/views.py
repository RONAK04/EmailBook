from .serializers import userSerializer
from rest_framework.generics import ListAPIView
from .models import User

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
