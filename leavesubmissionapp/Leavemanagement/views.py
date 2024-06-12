from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import LeaveApplicationSerializer
from .models import *
# Create your views here.

User = get_user_model()

class LeaveSubmissionView(generics.CreateAPIView):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer

class RetrieveLeaveDetailsView(generics.ListAPIView):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer

class RetrieveSingleLeaveDetailView(generics.ListAPIView):
    serializer_class = LeaveApplicationSerializer

    def get_queryset(self):
        applicant_id = self.kwargs.get('applicant_id')
        return LeaveApplication.objects.filter(applicant_id=applicant_id)