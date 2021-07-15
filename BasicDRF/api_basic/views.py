from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Artical
from .serializers import ArticalSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


# function to view list of all models and
# create a new model
@api_view(['GET', 'POST'])
def artical_list(request):
    if request.method == "GET":
        # fetch all Articals from database
        articals = Artical.objects.all()
        # Now we need to serialize the articals such that return type is json
        serializer = ArticalSerializer(articals, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticalSerializer(data=request.data)

        # check if serialize is valid as our schema or not
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if shema posted is not valid then retun 400 as bad request
        else:
            return Response(serializer.errors, status=status.HTTP_400)


# Function to Retrive , Update, and delete model
@api_view(["GET", "PUT", "DELETE"])
def artical_detail(request, pk):
    """
    Retrive Update and delete data
    """
    try:
        artical = Artical.objects.get(pk=pk)
    except Artical.DoesNotExist:
        return Response(content="Sorry endpoint  does not exist", status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serializer = ArticalSerializer(artical)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticalSerializer(artical, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400)

    elif request.method == "DELETE":
        artical.delete()
        return Response(content="Deleted successfully", status=status.HTTP_204_NO_CONTENT)
