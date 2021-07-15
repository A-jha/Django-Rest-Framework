# Writing regular Django views using our Serializer

## Function Based Views

### function to view list of all models and create a new model

```py
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

## Rest framework api_views(allows us to use api debug browser support)
