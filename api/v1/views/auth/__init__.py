from rest_framework.views import APIView
from rest_framework.response import Response

class TodoListApiView(APIView):
    def get(self,request):
        data = {}
        data['message'] = "Testing"
        return Response(data)

class test_params(APIView):
    def get(self,request,*args,**kwargs):
        # filter = self.kwargs['filter']
        filter = request.GET.get("filter","")
        test_item = request.GET.get("testitem","")
        # test_item = self.kwargs['testitem']
        # category = self.kwargs['category_id']
        data = {}
        data['test-item'] = test_item
        data['filter'] = filter
        data['message'] = "Testing"
        return Response(data)