from django.test import TestCase
from django.urls import reverse,resolve
from Leavemanagement.views import *



class TestUrls(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(user_name='testuser', role='employee', email='sample@sample.com', password='password')

        self.leave = LeaveApplication.objects.create(
            applicant=self.user,
            startdate='2024-06-12',
            enddate='2024-06-14',
            type_of_leave='vacation'
        )



    def test_leave_submission(self):
        url = reverse('leave_submission')
        self.assertEquals(resolve(url).func.view_class, LeaveSubmissionView)



    def test_retrieving_all_leave_details(self):
        url = reverse('leave_details')
        self.assertEquals(resolve(url).func.view_class, RetrieveLeaveDetailsView)



    def test_retrieving_leave_details_of_a_single_employee(self):
        url = reverse('single_leave_detail', kwargs={'applicant_id': self.user.id})
        self.assertEquals(resolve(url).func.view_class, RetrieveSingleLeaveDetailView)



    def test_accepting_leave(self):
        url = reverse('accept_leave', kwargs={'leave_id': self.leave.id})
        self.assertEquals(resolve(url).func.view_class, LeaveAcceptingView)



    def test_declining_leave(self):
        url = reverse('decline_leave', kwargs={'leave_id': self.leave.id})
        self.assertEquals(resolve(url).func.view_class, LeaveDecliningView)