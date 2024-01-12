from django.shortcuts import render,redirect
from .models import product
from .serializers import productserializers
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
@api_view(["POST"])
def add(request):
    
    if request.method=="POST":
        serializer=productserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        

    
def search(request):

    if request.method=="POST":
        location=request.POST["location"]
        pro=product.objects.all()
        mydata=product.objects.filter(location=location).values
        
            
        return render(request,"display.html",{"mydata":mydata})
            
    return render(request,"search.html")
@api_view(["GET","PUT","DELETE"])
def productid(request,id):
    try:
        p=product.objects.get(pk=id)
    except p.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=productserializers(p)
        return JsonResponse(serializer.data)
    if request.method=="PUT":
        serializer=productserializers(p,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=="DELETE":
        p.delete()
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
@api_view(["GET"])
def products(request):
    if request.method=="GET":
        pro=product.objects.all()
        serializer=productserializers(pro,many=True)
        return JsonResponse(serializer.data,safe=False)




