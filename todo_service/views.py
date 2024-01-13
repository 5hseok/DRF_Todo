from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSimpleSerializer, TodoDetailSerializer, TodoCreateSerializer
import time
class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complete = False)      # complete가 False인 Todo들은 필터링 
        serializer = TodoSimpleSerializer(todos, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    def post(self, request):
        serializer = TodoDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
class TodoAPIView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoCreateSerializer(todo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DoneTodosAPIView(APIView):
    def get(self, request):
        dones = Todo.objects.filter(complete = True)      # complete가 False인 Todo들은 필터링 
        serializer = TodoSimpleSerializer(dones, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
class DoneTodoAPIView(APIView):
    def put(self, request, pk):
        done = get_object_or_404(Todo, id=pk)
        done.complete = True
        done.completed_time = time.time()
        done.save()
        serializer = TodoDetailSerializer(done)
        return Response(serializer.data, status=status.HTTP_200_OK)