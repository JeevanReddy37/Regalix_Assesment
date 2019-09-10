from rest_framework.viewsets import ModelViewSet
from .models import TaskDetails
from .serializers import TaskSerializer

class TaskViewSet(ModelViewSet):

    queryset = TaskDetails.objects.all()
    serializer_class = TaskSerializer