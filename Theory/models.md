# Models

A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

## Setup

Step1: Cteate your models in models.py

```py
class Artical(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

Step2: Register your Models inside admin.py file so that you can view it in admin pannel

```py
admin.site.register(Artical)
```

## Now We have to write serializers based on our schema so that API can send and receive a right format of data.
