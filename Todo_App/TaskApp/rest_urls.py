from django.conf.urls import url,include
from .viewsets import TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('task_details', TaskViewSet)

urlpatterns = [

    url(r'',include(router.urls))
]

urlpatterns += router.urls