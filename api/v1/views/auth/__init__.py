from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.response import Response

from rest_framework import permissions, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializer import RegisterSerializer, UserSerializer, MyTokenObtainPairSerializer

from accounts.models import User


class TodoListApiView(APIView):
    def get(self,request):
        data = {}
        data['message'] = "Testing"
        return Response(data)


class TestParams(ListAPIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        try:
            data = {}
            # filter = self.kwargs['filter']
            filter = self.request.GET.get("filter","")
            test_item = self.request.GET.get("testitem","")
            data['test-item'] = test_item
            data['filter'] = filter
            data['message'] = "Testing"
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


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    

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