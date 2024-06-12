from django.urls import path
from .views import LeaveSubmissionView,RetrieveLeaveDetailsView,RetrieveSingleLeaveDetailView
urlpatterns = [
    path('leavesubmission/',LeaveSubmissionView.as_view(),name='leave_submission'),
    path('retrievallleavedetails/',RetrieveLeaveDetailsView.as_view(),name='leave_details'),
    path('retrieveleavedetails/<int:applicant_id>/',RetrieveSingleLeaveDetailView.as_view(),name='single_leave_detail')
    
]
