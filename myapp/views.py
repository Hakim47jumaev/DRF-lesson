from .models import Book,Author,Car,Product
from .serializers import BookSerilizer,AuthorSerializer,CarSerializer,ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .filter import price_filter
from .search import search_by_title
from .pagination import CastomPagination
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
 
class Cars(ListCreateAPIView):
    queryset=Car.objects.all()
    serializer_class=CarSerializer

class CarsById(RetrieveUpdateDestroyAPIView):
    queryset=Car.objects.all()
    serializer_class=CarSerializer

class Products(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer



class BookListCreateAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerilizer(books, many=True)
        return Response(serializer.data)
    @swagger_auto_schema(
        request_body=BookSerilizer,
        responses={201: BookSerilizer}
    )
    def post(self, request):
        serializer = BookSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET','DELETE','PUT'])
def book(request,id):
    try:
        book=Book.objects.get(id=id)

    except Book.DoesNotExist:
        return Response({"key":'not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=BookSerilizer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method =='PUT':
        data=request.data
        serializer=BookSerilizer(book,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='DELETE':
        book.delete()
        return Response({"key":'deleted'},status=status.HTTP_204_NO_CONTENT)


 


class AuthorListCreateView(GenericAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
