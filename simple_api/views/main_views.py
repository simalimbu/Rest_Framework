from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from ..searializers import CategorySerializer,ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from ..models import Category,Product

#function-based
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def category_view(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Category added successfully!!"},status=status.HTTP_201_CREATED)
        else:
            return Response({'msg':"Failed to add category!",'err':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'GET':
        category = Category.objects.all()
        serializer =  CategorySerializer(category, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)