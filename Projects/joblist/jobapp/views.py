from rest_framework.viewsets import ModelViewSet
from .models import Job
from .serializers import JobSerializer

# Create your views here.


# def index(request):
#     return HttpResponse("Hello, world. You're at the Job app index.")


class JobsViewSet(ModelViewSet):
    queryset= Job.objects.all()
    serializer_class=JobSerializer

 

 