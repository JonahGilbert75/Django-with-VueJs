from rest_framework.serializers import ModelSerializer

from .models import Job
class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields= ['id','Company_name','Title','Job_Nature','Salary','No_of_post','Name']


