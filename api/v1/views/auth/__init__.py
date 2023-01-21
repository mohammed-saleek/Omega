from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.response import Response

# from django.contrib.auth.models import User
from accounts.models import User

from rest_framework import permissions, mixins
from .serializer import RegisterSerializer, UserSerializer


class TodoListApiView(APIView):
    def get(self,request):
        data = {}
        data['message'] = "Testing"
        return Response(data)


class test_params(APIView):
    def get(self,request,*args,**kwargs):
        try:
            data = {}
            # filter = self.kwargs['filter']
            filter = request.GET.get("filter","")
            test_item = request.GET.get("testitem","")
            data['test-item'] = test_item
            data['filter'] = filter
            data['message'] = "Testing"
            # return Response(data)
        except Exception as exception:
            data['error'] = str(exception)
            data['status'] = 'Failed'
        return Response(data)
    
class UserRegistration(GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


class ListUser(ListAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        users = User.objects.all()
        return users
        

# class ListUser(ListAPIView):
#     def get(self,request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)