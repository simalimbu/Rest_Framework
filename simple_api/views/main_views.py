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
     
#For Product     
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def product_view(request):
    if request.method == 'POST':
        searializer = ProductSerializer(data=request.data)
        if searializer.is_valid():
            searializer.save(user=request.user)   #user ko id  pass garxa
            return Response({'msg': "Product added successffully",'product':searializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'msg':"Failed to add product",'err':searializer.errors},status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        try:
            product = Product.objects.all()
            searializer = ProductSerializer(product, many=True)
            return Response(searializer.data,status=status.HTTP_200_OK) 
        except Exception as e:
            return Response({'msg':"Failed to fetch data",'err':e})


#For Product by id
@api_view(['PUT','DELETE', 'GET'])
@permission_classes([IsAuthenticated])
def productby_id(request,id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({'msg':"Product does not exist"})
    
    if request.method == 'PUT':
        searializer = ProductSerializer(product, data=request.data, partial=True)
        if searializer.is_valid():
            searializer.save()
            return Response({'msg':"Product updated successfully!!"},status=status.HTTP_200_OK)
        else: 
            return Response({'msg':"Failed to update product", 'err':searializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        searializer = ProductSerializer(product)
        return Response({'data':searializer.data},status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response({'msg':"Product deleted successfully"},status=status.HTTP_200_OK)

    else:
        return Response({'msg':"Invalid request"},status=status.HTTP_400_BAD_REQUEST)
    
#To get product in each category
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_products(request,category_id):
    if request.method == 'GET':
        product = Product.objects.filter(category=category_id)
        serializer = ProductSerializer(product, many=True)
        return Response({'data':serializer.data},status=status.HTTP_200_OK)
    else:
        return Response({'msg':"Umable to fetch data"},status=status.HTTP_400_BAD_REQUEST)
    
#To get category and product
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_with_products(request):
    categories = Category.objects.all() 
    data = []

    for category in categories:
        products = Product.objects.filter(category=category)
        if products.exists():
            category_data = CategorySerializer(category).data
            product_data = ProductSerializer(products, many=True).data
            category_data['products'] = product_data
            data.append(category_data)

    return Response({'data': data}, status=status.HTTP_200_OK)