from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Users
from .models import Roles
from .serializers import UsersSerializer
from .serializers import RolesSerializer


def get_object(pk):
    try:
        return Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        raise Http404


class UserList(APIView):

    def get(self, request):
        user = Users.objects.all()
        serializer = UsersSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get(self, request, pk):
        user = get_object(pk)
        serializer = UsersSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object(pk)
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoleList(APIView):
    def get(self, request):
        role = Roles.objects.all()
        serializer = RolesSerializer(role, many=True)
        return Response(serializer.data)


class RoleDetail(APIView):
    def get(self, request, pk):
        user = Users.objects.filter(roles=pk)
        serializer = UsersSerializer(user, many=True)
        return Response(serializer.data)
