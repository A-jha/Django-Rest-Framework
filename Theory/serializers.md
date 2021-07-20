# Creating a Serializer class

The first thing we need to get started on our Web API is to provide a way of serializing and deserializing the snippet instances into representations such as json. We can do this by declaring serializers that work very similar to Django's forms. Create a file in the snippets directory named serializers.py

# 1.Normal Serializer

```py
class ArticalSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    # create methods
    def create(self, validated_data):
        return Artical.objects.create(validated_data)

    # update
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)

        instance.save()
        return instance
```

- > The first part of the serializer class defines the fields that get serialized/deserialized. The create() and update() methods define how fully fledged instances are created or modified when calling serializer.save()

- > We can actually also save ourselves some time by using the ModelSerializer class

## Working with Serializers

```bash
avinashjha@Siya:~/Desktop/DJANGO-ALL/DRF-BASICS/BasicDRF$ python3 manage.py shell
Python 3.8.10 (default, Jun  2 2021, 10:49:15)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from api_basic.models import Artical
>>> from api_basic.serializers import ArticalSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser

### Create an Artical a
>>> a = Artical(title="Artical Title", author="dada", email="jha@gmail.com")
>>> a.save()

### Create an Artical b
>>> b = Artical(title="Artical Title 3", author="dadag", email="jhaaa@gmail.com")
>>> b.save()

### Render data in dictionary format
>>> serializer = ArticalSerializer(a)
>>> serializer.data
{'title': 'Artical Title', 'author': 'dada', 'email': 'jha@gmail.com', 'date': '2021-07-15T06:39:53.399514Z'}

### To finalize the serialization process we render the data into json.
>>> content = JSONRenderer().render(serializer.data)
b'{"title":"Artical Title","author":"dada","email":"jha@gmail.com","date":"2021-07-15T06:39:53.399514Z"}'

### All object are together
>>> serializer = ArticalSerializer(Artical.objects.all(),many=True)
>>> serializer.data
[OrderedDict([('title', 'Artical Title'), ('author', 'dada'), ('email', 'jha@gmail.com'), ('date', '2021-07-15T06:39:53.399514Z')]), OrderedDict([('title', 'Artical Title 3'), ('author', 'dadag'), ('email', 'jhaaa@gmail.com'), ('date', '2021-07-15T06:40:40.545435Z')])]

### Representation of Artical serializer

>>> serializer = ArticalSerializer()
>>> print(repr(serializer))
ArticalSerializer():
    title = CharField(max_length=100)
    author = CharField(max_length=100)
    email = EmailField(max_length=100)
    date = DateTimeField()
```

---

# 2. Using Model Serializers

Our SnippetSerializer class is replicating a lot of information that's also contained in the Snippet model. It would be nice if we could keep our code a bit more concise.

In the same way that Django provides both Form classes and ModelForm classes, REST framework includes both Serializer classes, and ModelSerializer classes.

```py
class ArticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artical
        fields = ['id', 'title', 'author']
```

### If we view the reprwsentation of model serializer

```bash
>>> serializer = ArticalSerializer()
>>> print(repr(serializer))
ArticalSerializer():
    title = CharField(max_length=100)
    author = CharField(max_length=100)
    email = EmailField(max_length=100)
    date = DateTimeField()
```

This looks similar to our default serializer.
