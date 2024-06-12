from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import LeaveApplicationSerializer,LeaveApplicationUpdateSerializer
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

class LeaveAcceptingView(APIView):
    def patch(self, request, leave_id):
        try:
            leave_application = LeaveApplication.objects.get(id=leave_id)
        except LeaveApplication.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        leave_application.status = 'leave granted'
        leave_application.save()
        serializer = LeaveApplicationUpdateSerializer(leave_application)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LeaveDecliningView(APIView):
    def patch(self, request, leave_id):
        try:
            leave_application = LeaveApplication.objects.get(id=leave_id)
        except LeaveApplication.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        leave_application.status = 'leave declined'
        leave_application.save()
        serializer = LeaveApplicationUpdateSerializer(leave_application)
        return Response(serializer.data, status=status.HTTP_200_OK)