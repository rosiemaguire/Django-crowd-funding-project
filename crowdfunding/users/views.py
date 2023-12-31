from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import UserUpdatePermission

class CustomUserList(APIView):
    
    def get(self,request):
        if request.user.is_staff:
            users = CustomUser.objects.all()
            serializer = CustomUserSerializer(users, many=True)
            return Response(serializer.data)
        elif request.user.is_authenticated:
            users = CustomUser.objects.all().get(pk=self.request.user.id)
            data = CustomUserSerializer.get_restricted_data(users)
            serializer = CustomUserSerializer(users, data=data,many=True)
            return Response(serializer.initial_data)
        else:
            return Response(
                { "detail": "You do not have permission to perform this action." }, 
                status=status.HTTP_401_UNAUTHORIZED
            )
            
    
    def post(self,request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_staff:
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            else:
                serializer.save(
                    is_staff=False,
                    is_superuser=False
                )
                user = CustomUser.objects.all().get(pk=serializer.data['id'])
                data = CustomUserSerializer.get_restricted_data(user)
                results_returned = CustomUserSerializer(user,data=data)
                return Response(
                    results_returned.initial_data,
                    status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class CustomUserDetail(APIView):
    permission_classes = [UserUpdatePermission]

    def get_object(self,pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            self.check_object_permissions(self.request,user)
            return user
        except CustomUser.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        user = self.get_object(pk)
        self.check_object_permissions(self.request,user)
        if request.user.is_staff:
            serializer = CustomUserSerializer(user)
            return Response(serializer.data)
        else:
            data = CustomUserSerializer.get_restricted_data(user)
            serializer = CustomUserSerializer(user,data=data)
            return Response(serializer.initial_data)
    
    def put(self,request,pk):
        user = self.get_object(pk)      
        serializer = CustomUserSerializer(
            instance=user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class CurrentUserView(APIView):
    def get(self, request):
        if request.user.is_staff:
            serializer = CustomUserSerializer(request.user)
            return Response(serializer.data)
        elif request.user.is_authenticated:
            data = CustomUserSerializer.get_restricted_data(request.user)
            serializer = CustomUserSerializer(request.user,data=data)
            return Response(serializer.initial_data)
        else:
            return Response(
                { "detail": "You are not currently logged in." }, 
                status=status.HTTP_404_NOT_FOUND
            )