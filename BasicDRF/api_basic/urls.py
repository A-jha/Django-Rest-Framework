from django import urls
from django.urls import path, include
from .views import artical_list, artical_detail, ArticalApiView, ArticalDetails, GenericAPIView, ArticalViewSet, ArticalGenericViewset, ArticalModelViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticalViewSet, basename="article")
router.register('generic', ArticalGenericViewset, basename="generic")
router.register('genericmodal', ArticalModelViewset, basename="generic modal")
urlpatterns = [
    path("viewset/", include(router.urls)),
    path("viewset/<int:pk>", include(router.urls)),
    path('', artical_list),
    path('details/<int:pk>/', artical_detail),
    path("capi/", ArticalApiView.as_view()),
    path("capid/<int:id>/", ArticalDetails.as_view()),
    path("generic/", GenericAPIView.as_view()),
    path("generic/<int:id>/", GenericAPIView.as_view())
]
