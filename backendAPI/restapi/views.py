from .models import Camp
from .serializers import CampSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CampList(APIView):

    def get(self,reqest):
        camp = Camp.objects.all()
        serializer = CampSerializer(camp, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CampSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Create your views here.

