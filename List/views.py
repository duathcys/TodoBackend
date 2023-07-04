from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializer import TodoSerializer


@api_view(['GET', 'POST'])
def todo_List(request):
    if request.method == 'GET':
        filter_todos = request.GET.get('info', None)
        print('filter', filter_todos)
        todoss = Todo.objects.select_related('info').filter(info=filter_todos)
        serializer = TodoSerializer(todoss, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_Detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
        print('pk', pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        print(request.data)
        serializer = TodoSerializer(todo, data=request.data)
        print(request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def check_todo(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    done = request.data.get('done')
    if done is not None:
        todo.done = bool(done)
        todo.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)



