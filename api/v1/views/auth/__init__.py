from rest_framework.views import APIView
from rest_framework.response import Response

class TodoListApiView(APIView):
    def get(self,request):
        data = {}
        data['message'] = "Testing"
        return Response(data)