# Writing regular Django views using our Serializer

## Function Based Views

### function to view list of all models and create a new model

```py
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Artical
from .serializers import ArticalSerializer
from django.views.decorators.csrf import csrf_exempt
# function to view list of all models and
# create a new model
@csrf_exempt ## Post which don't have csrf token can be allowed
def artical_list(request):
    if request.method == "GET":
        # fetch all Articals from database
        articals = Artical.objects.all()
        # Now we need to serialize the articals such that return type is json
        serializer = ArticalSerializer(articals, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        # create a data
        data = JSONParser().parse(request)
        serializer = ArticalSerializer(data=data)

        # check if serialize is valid as our schema or not
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        # if shema posted is not valid then retun 400 as bad request
        else:
            return JsonResponse(serializer.errors, status=401)
```

### Function to Retrive , Update, and delete model

```py
from .models import Artical
from .serializers import ArticalSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Function to Retrive , Update, and delete model
@csrf_exempt ## Post which don't have csrf token can be allowed
def artical_detail(request, pk):
    """
    Retrive Update and delete data
    """
    try:
        artical = Artical.objects.get(pk=pk)
    except Artical.DoesNotExist:
        return HttpResponse(content="Sorry endpoint  does not exist", status=404)

    if request.method == "GET":
        serializer = ArticalSerializer(artical)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticalSerializer(artical, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=202)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        artical.delete()
        return JsonResponse(content="Deleted successfully", status=204)

```

> > > > **Rest framework api_views(allows us to use api debug browser support**

# class based views in DRF

```py
from .models import Artical
from .serializers import ArticalSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# import APICiew for claased based views
from rest_framework.views import APIView

# Create your views here.
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
```

# DRF Generic View

Django’s generic views... were developed as a shortcut for common usage patterns... They take certain common idioms and patterns found in view development and abstract them so that you can quickly write common views of data without having to repeat yourself.

The generic views provided by REST framework allow you to quickly build API views that map closely to your database models.

```py
# use generic view
from rest_framework import generics
from rest_framework import mixins

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
```
