from rest_framework import serializers
from .models import LeaveApplication

class LeaveApplicationSerializer(serializers.ModelSerializer):
    applicant_user_name = serializers.SerializerMethodField() 
    total_leaves_by_applicant = serializers.SerializerMethodField()
    class Meta:
        model = LeaveApplication
        fields = ['id', 'type_of_leave', 'startdate', 'enddate', 'status', 'applicant', 'applicant_user_name','total_leaves_by_applicant']

    def get_applicant_user_name(self, obj):
        return obj.applicant.user_name

    def get_total_leaves_by_applicant(self, obj):
        return LeaveApplication.objects.filter(applicant=obj.applicant).count()

class LeaveApplicationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplication
        fields = '__all__'