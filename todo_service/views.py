from rest_framework import generics
from rest_framework import viewsets
from .serializers import TodoSimpleSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Todo

class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complete = False)      # complete가 False인 Todo들은 필터링 
        serializer = TodoSimpleSerializer(todos, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)


# Create your views here.
