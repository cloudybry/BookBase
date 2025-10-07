from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Prompt
from .serializers import PromptSerializer
from django.shortcuts import render
from rest_framework import generics

@swagger_auto_schema(
    method='post',
    request_body=PromptSerializer,
    responses={201: PromptSerializer}
)
@api_view(['GET', 'POST'])
def prompt_list_create(request):
    if request.method == 'GET':
        prompts = Prompt.objects.all()
        serializer = PromptSerializer(prompts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return render(request, 'home.html')

class PromptListCreate(generics.ListCreateAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer

class PromptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer

# 🛠️ New view for update and delete
@api_view(['PUT', 'DELETE'])
def prompt_detail(request, pk):
    try:
        prompt = Prompt.objects.get(pk=pk)
    except Prompt.DoesNotExist:
        return Response({'error': 'Prompt not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PromptSerializer(prompt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        prompt.delete()
        return Response({'message': 'Prompt deleted'}, status=status.HTTP_204_NO_CONTENT)