from rest_framework import serializers
from .models import Company, Team

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('UUID','name', 'CEO', 'address', 'Inception_date')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('UUID','CompanyID', 'Lead_Name')