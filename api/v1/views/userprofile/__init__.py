from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import (
    ListAPIView, DestroyAPIView, CreateAPIView, 
    UpdateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
)
from rest_framework.response import Response

from userprofile.models import Profile, EducationDetails, ProfessionDetails
from api.v1.views.userprofile.serializer import UserProfileSerializerList

#write your view classes here
class ProfileListView(ListAPIView):
    serializer_class = UserProfileSerializerList
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self, *args, **kwargs):
        data = {}
        try:
            queryset = Profile.objects.all()

            return queryset
        except Exception as exception:
            data["status"] = "failed"
            data["message"] = str(exception)
            return Response(data, status=500)


class ProfileCreateView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        data = request.data.get("data")
        print(data)
        return Response(data)