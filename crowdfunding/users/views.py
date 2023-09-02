from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import UserUpdatePermission

class CustomUserList(APIView):
    # def get_queryset(self, request):
    #     if request.user.is_staff:
    #         return CustomUser.objects.all()
    #     else:
    #         users = CustomUser.objects.all()
    #         users = users.values('username','first_name','last_name','email','date_joined')
    #         users = users.filter(pk=self.request.user.id)
    #         return users
    
    # def get(self,request):
    #     users = self.get_queryset(request)
    #     serializer = CustomUserSerializer(users, many=True)
    #     return Response(serializer.data)
    
    def get(self,request):
        if request.user.is_staff:
            users = CustomUser.objects.all()
            serializer = CustomUserSerializer(users, many=True)
            return Response(serializer.data)
        else:
            users = CustomUser.objects.all()
            
            # users = users.values('username','first_name','last_name','email','date_joined','last_login')
            users = users.get(pk=self.request.user.id)
            data = CustomUserSerializer.get_restricted_data(users)
            serializer = CustomUserSerializer(users, data=data,many=True)
            return Response(serializer.initial_data)
    
    def post(self,request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_staff:
                serializer.save()
            else:
                serializer.save(
                    is_staff=False,
                    is_superuser=False
                )
                serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class CustomUserDetail(APIView):
    permission_classes = [UserUpdatePermission]

    # def get_restricted_data(self,instance):
    #     return {
    #         'username': instance.username,

    #     }
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
        # if request.user.is_staff:
        #     return Response(serializer.data)
        # else:
        
    
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