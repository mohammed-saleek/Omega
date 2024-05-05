from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import (
    ListAPIView, DestroyAPIView, CreateAPIView, 
    UpdateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
)
from rest_framework.response import Response

from userprofile.models import (
    Profile, EducationDetails, ProfessionDetails, Address
)
from api.v1.views.userprofile.serializer import (
    UserProfileListSerializer, AddressCreateSerializer, ProfileCreateSerializer
)

#write your view classes here
class ProfileListView(ListAPIView):
    serializer_class = UserProfileListSerializer
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
        response = {
            "message": "Profile has been created.",
            "status": "success"
        }
        try:
            data = request.data.get("data")
            address = request.data.get("address")
            
            #serializer for creating a new address
            serializer = AddressCreateSerializer(data=address)
            if serializer.is_valid():
                address_obj = serializer.save()
            
            #set value for address and user
            data["address"] = address_obj.id
            data["user"] = request.user.id
            
            #serializer for creating profile
            serializer_data = ProfileCreateSerializer(data=data)
            if serializer_data.is_valid():
                serializer_data.save()
            return Response(response, status=200)
        except Exception as exception:
            response["message"] = "Profile creation failed"
            response["status"] = "failed"
            return Response(response, status=500)