from .models import Artical
from .serializers import ArticalSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# import APICiew for claased based views
from rest_framework.views import APIView

# use generic view
from rest_framework import generics
from rest_framework import mixins

# authentication
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# ViewSets
from rest_framework import viewsets

from django.shortcuts import get_object_or_404
# Create your views here.
#------------Modal View set-------------#


class ArticalModelViewset(viewsets.ModelViewSet):
    serializer_class = ArticalSerializer
    queryset = Artical.objects.all()

#-----------generic Viewset------------#


class ArticalGenericViewset(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.RetrieveModelMixin):
    serializer_class = ArticalSerializer
    queryset = Artical.objects.all()

#------------ViewSets-----------------#


class ArticalViewSet(viewsets.ViewSet):
    name = "article"

    def list(self, request):
        articals = Artical.objects.all()
        serializer = ArticalSerializer(articals, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Artical.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticalSerializer(article)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def update(self, request, pk=None):
        artical = self.objects.get(pk=pk)
        serializer = ArticalSerializer(artical, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk):
        artical = self.objects.get(pk=pk)
        artical.delete()
        return Response(content="Deleted successfully", status=status.HTTP_204_NO_CONTENT)

#-----------Generic Api View----------------#


class GenericAPIView(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin):

    serializer_class = ArticalSerializer
    queryset = Artical.objects.all()
    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, id=None):
        return self.create(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

#---------------Class Based View-------------------#


class ArticalApiView(APIView):

    def get(self, request):
        articals = Artical.objects.all()
        serializer = ArticalSerializer(articals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400)


class ArticalDetails(APIView):
    def get_object(self, id):
        try:
            return Artical.objects.get(id=id)
        except Artical.DoesNotExist:
            return Response(content="Sorry endpoint  does not exist", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        artical = self.get_object(id)
        serializer = ArticalSerializer(artical)
        return Response(serializer.data)

    def put(self, request, id):
        artical = self.objects.get(id)
        serializer = ArticalSerializer(artical, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, id, request):
        artical = self.objects.get(id)
        artical.delete()
        return Response(content="Deleted successfully", status=status.HTTP_204_NO_CONTENT)

#----------------Function Based View-----------------#
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
