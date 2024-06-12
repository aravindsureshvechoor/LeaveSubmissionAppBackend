from django.test import TestCase,Client
from Leavemanagement.serializers import *
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
import json


User = get_user_model()






class TestLeaveSubmissionView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(user_name='testuser',role='employee',email='sample@sample.com',password='password')
    
    def test_successful_leave_submission(self):
        leave_application = {
            'applicant': self.user.id,  
            'startdate': '2024-06-12',
            'enddate': '2024-06-14',
            'type_of_leave': 'vacation',
        }
        url = reverse('leave_submission')
        
        response    = self.client.post(url,data=leave_application,format='json')

        self.assertEqual(response.status_code,201)

    # invalid data
    def test_invalid_leave_submission(self):
        leave_application = {
            'startdate': '2024-06-12',
            'enddate': '2024-06-14',
            'type_of_leave': 'vacation',
        }
        url = reverse('leave_submission')
        
        response    = self.client.post(url,data=leave_application,format='json')

        self.assertEqual(response.status_code,400)






class RetrieveLeaveDetailsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(user_name='testuser', role='employee', email='sample@sample.com', password='password')

        self.leave = LeaveApplication.objects.create(
            applicant=self.user,
            startdate='2024-06-12',
            enddate='2024-06-14',
            type_of_leave='vacation'
        )

    def test_retrieve_leave_details(self):

        url = reverse('leave_details')

        response = self.client.get(url)

        self.assertEqual(response.status_code,200)







class RetrieveLeaveDetailsForSingleEmployeeTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(user_name='testuser', role='employee', email='sample@sample.com', password='password')

        self.leave = LeaveApplication.objects.create(
            applicant=self.user,
            startdate='2024-06-12',
            enddate='2024-06-14',
            type_of_leave='vacation'
        )

    def test_retrieve_leave_details(self):

        url = reverse('single_leave_detail',kwargs={'applicant_id': self.user.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code,200)







class LeaveAcceptingViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(user_name='testuser', role='employee', email='sample@sample.com', password='password')
        self.client.login(username='testuser', password='password')

        self.leave_application = LeaveApplication.objects.create(
            applicant=self.user,
            startdate='2024-06-12',
            enddate='2024-06-14',
            type_of_leave='vacation',
            status='pending'
        )





    def test_leave_acceptance(self):
        url = reverse('accept_leave', kwargs={'leave_id': self.leave_application.id})

        response = self.client.patch(url)

        self.assertEqual(response.status_code, 200)

    def test_leave_rejection(self):
        url = reverse('decline_leave', kwargs={'leave_id': self.leave_application.id})

        response = self.client.patch(url)

        self.assertEqual(response.status_code, 200)