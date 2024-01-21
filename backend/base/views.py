from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Book
from base.serializers import BookSerializer




@api_view(['GET','POST','DELETE','PUT','PATCH'])
def books(req,id=-1):
    if req.method =='GET':
        if id > -1:
            try:
                temp_book=Book.objects.get(id=id)
                return Response (BookSerializer(temp_book,many=False).data)
            except Book.DoesNotExist:
                return Response ("not found")
        all_books=BookSerializer(Book.objects.all(),many=True).data
        return Response ( all_books)
    if req.method =='POST':
        tsk_serializer = BookSerializer(data=req.data)
        if tsk_serializer.is_valid():
            tsk_serializer.save()
            return Response ("posted")
        else:
            return Response (tsk_serializer.errors)
    if req.method =='DELETE':
        try:
            temp_book=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response ("not found")    
       
        temp_book.delete()
        return Response ("deleted")
    if req.method =='PUT':
        try:
            temp_book=Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response ("not found")
       
        ser = BookSerializer(data=req.data)
        old_Book = Book.objects.get(id=id)
        res = ser.update(old_Book, req.data)
        return Response(res)
    