from .models import Book
from .serializers import BookSerilizer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def books(request):
    if request.method=='GET':
        books=Book.objects.all()
        serializer=BookSerilizer(books,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

 
    if request.method=='POST':
        serilizer=BookSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)


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


 
