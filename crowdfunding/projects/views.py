from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project,Pledge
from .serializers import ProjectSerializer,PledgeSerializer,ProjectDetailSerializer, PledgeDetailSerializer
from django.http import Http404
from rest_framework import status, permissions, generics
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly

class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self,request):
        projects = Project.objects.all().filter(is_deleted=False)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                owner=request.user,
                is_deleted=False,
                is_open=True
            )
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self,pk):
        try:
            projects = Project.objects.all().filter(is_deleted=False)
            project = projects.get(pk=pk)
            # project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request,project)
            project.pledges.all().filter(is_deleted=True).delete()
            return project
        except Project.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    def put(self,request,pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(
            instance=project,
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

class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self,request):
        pledges = Pledge.objects.all().filter(is_deleted=False)
        serializer = PledgeSerializer(pledges,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        pledge = request.data
        project = Project.objects.get(pk=pledge['project'])
        serializer = PledgeSerializer(data=request.data)
        if project.is_open == True:
            if serializer.is_valid():
                serializer.save(
                    supporter=request.user,
                    is_deleted=False
                )
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(
                { 'message': "Project is not open" },                
                status=status.HTTP_400_BAD_REQUEST
            )

class PledgeDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsSupporterOrReadOnly
    ]

    def get_object(self,pk):
        try:
            pledges = Pledge.objects.all().filter(is_deleted=False)
            pledge = pledges.get(pk=pk)
            # pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request,pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledge)
        return Response(serializer.data)

    def put(self,request,pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(
            instance=pledge,
            data=request.data,
            partial=True
        )
        if pledge.project.is_open == True:
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
        return Response(
            { 'message': "Project is not open" },
            status=status.HTTP_400_BAD_REQUEST
            )

class PledgeDeleteView(generics.DestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAdminUser
    ]

    def get_object(self,pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request,pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404
    
    def delete(self,request,pk):
        pledge = self.get_object(pk)
        pledge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectDeleteView(generics.DestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAdminUser
    ]

    def get_object(self,pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request,project)
            return project
        except Project.DoesNotExist:
            raise Http404
    
    def delete(self,request,pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserProjectView(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            projects = Project.objects.all().filter(is_deleted=False,owner=request.user)
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data)
        else:
            return Response({ "detail": "No projects to view." })

class UserPledgeView(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            pledges = Pledge.objects.all().filter(is_deleted=False,supporter=request.user)
            serializer = PledgeSerializer(pledges,many=True)
            return Response(serializer.data)
        else:
            return Response({ "detail": "No pledges to view." })
    