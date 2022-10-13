from django.shortcuts import render
from rest_framework import status
#from .serializers import Inputserializer
from rest_framework.decorators import action
from rest_framework.response import Response
#from .models import Input
from .predict import Predict
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication



class InputViewSet(APIView):
    #serializer_class = Inputserializer
    #queryset = Input.objects.all()
    #authentication_classes = (BasicAuthentication,)

    def post(self,request):
        if request.data:
            obj = Predict()
            k=obj.predict(request.data)
            #Input.objects.all().delete()

            return Response({'Input':request.data['String'],'Prediction':k},status=status.HTTP_200_OK)
        else:
            return Response({'Error':'String input is required.'},status=status.HTTP_400_BAD_REQUEST)







# Create your views here.
