from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSimpleSerializer, TodoDetailSerializer
class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complete = False)      # complete가 False인 Todo들은 필터링 
        serializer = TodoSimpleSerializer(todos, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class TodoAPIView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status = status.HTTP_200_OK)
        