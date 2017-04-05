from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import PoemSerializer
from .models import Poem
# from rest_framework.decorators import api_view
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# # from .permissions import IsOwnOrReadOnly
# from rest_framework import viewsets
# # Create your views here.
#
# class PoemMixin(object):
#     queryset = Poem.objects.all()
#     serializer_class = PoemSerializer
#     permission_classes = (IsOwnOrReadOnly,)
#
class PoemListView(APIView):
    def get(self,request,format=None):
        # poems=Poem.objects.all()
        poems=Poem.objects.filter(author='han')
        serializer=PoemSerializer(poems,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):

        serializer=PoemSerializer(data=request.data,many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class PoemDetailView(PoemMixin, RetrieveUpdateDestroyAPIView):
#     def perform_update(self, serializer):
#         serializer.save()
#
#
# class PoemViewSet(PoemMixin, viewsets.ModelViewSet):
#     pass
#
# poem_list = PoemViewSet.as_view(
#     {
#         'get':'list',
#         'post':'create',
#     }
# )
