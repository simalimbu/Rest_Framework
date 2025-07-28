from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from ..searializers import CategorySerializer,ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from ..models import Category,Product

#function-based
#For category
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
    
#For category by id
@api_view(['PUT','GET','DELETE'])
@permission_classes([IsAuthenticated])
def categoryby_id(request,id):
    
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response({'msg':"Category does not exist"})
    
    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Category updated successfully!!"},status=status.HTTP_200_OK)
        else:
            return Response({'msg':"Failed to update Category!!"},status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
       category = Category.objects.get(id=id)
       category.delete()
       return Response({'msg':"Blog deleted successfully!"},status=status.HTTP_400_BAD_REQUEST)
   
    elif request.method == 'GET':
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category)
        return Response({'data':serializer.data},status=status.HTTP_200_OK)
    
    else:
         return Response({'msg':"invalid request"},status=status.HTTP_400_BAD_REQUEST)
     