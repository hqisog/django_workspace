from django.conf.urls import url,include
from . import views
from rest_framework.routers import DefaultRouter

# poem_router = DefaultRouter()
# poem_router.register(r'poems', views.PoemViewSet)

urlpatterns = [
    # url(r'', include(poem_router.urls)),
    url(r'^poems/$', views.PoemListView.as_view(),name='poem_list'),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
]