# [Authentication & Permissions](https://www.django-rest-framework.org/api-guide/authentication/#basicauthentication)

Currently our API doesn't have any restrictions on who can edit or delete code snippets. We'd like to have some more advanced behavior in order to make sure that:

- Code snippets are always associated with a creator.
- Only authenticated users may create snippets.
- Only the creator of a snippet may update or delete it.
- Unauthenticated requests should have full read-only access.

# Basic Authentication

This authentication scheme uses HTTP Basic Authentication, signed against a user's username and password. Basic authentication is generally only appropriate for testing.

If successfully authenticated, BasicAuthentication provides the following credentials.

- request.user will be a Django User instance.
- request.auth will be None.

```py
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
```

- Then

```py
class GenericAPIView(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin):

    serializer_class = ArticalSerializer
    queryset = Artical.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
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
```

## Token based Authentication

This authentication scheme uses a simple token-based HTTP Authentication scheme. Token authentication is appropriate for client-server setups, such as native desktop and mobile clients.
