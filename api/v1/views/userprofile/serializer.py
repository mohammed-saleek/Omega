from rest_framework.serializers import (
    ModelSerializer, SerializerMethodField, CharField, IntegerField,
    DateTimeField
)
from userprofile.models import Profile
from api.v1.views.auth.serializer import UserSerializer

#serializer classes
class UserProfileSerializerList(ModelSerializer):
    user = SerializerMethodField(read_only=True)
    education = SerializerMethodField(read_only=True)
    profession = SerializerMethodField(read_only=True)
    
    def get_user(self, obj):
        try:
            data = {
                "email": obj.user.email,
                "username": obj.user.username,
                "first_name": obj.user.first_name,
                "last_name": obj.user.last_name,
                "is_active": obj.user.is_active,
                "licence_type": obj.user.licence_type.name
            }
            return data
        except Exception as exception:
            return None
    
    def get_education(self, obj):
        try:
            data = {
                "name": obj.education.name,
                "graduation_year": obj.education.graduation_year
            }
            return data
        except Exception as exception:
            return None
    
    def get_profession(self, obj):
        try:
            data = {
                "name": obj.profession.name,
                "company_name": obj.profession.company_name
            }
            return data
        except Exception as exception:
            return None
        
    class Meta:
        model = Profile
        fields = [
            "user",
            "education",
            "profession",
            "age",
            "phone_number"
        ]
        