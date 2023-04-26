from rest_framework import serializers
from .models import User
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'company_name', 'company_website', 'company_address', 'city', 'state', 'zip_code', 'country')
