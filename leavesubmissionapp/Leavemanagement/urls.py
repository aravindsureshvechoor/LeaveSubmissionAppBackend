from django.urls import path
from .views import LeaveSubmissionView,RetrieveLeaveDetailsView,RetrieveSingleLeaveDetailView,LeaveAcceptingView,LeaveDecliningView
urlpatterns = [
    path('leavesubmission/',LeaveSubmissionView.as_view(),name='leave_submission'),
    path('retrievallleavedetails/',RetrieveLeaveDetailsView.as_view(),name='leave_details'),
    path('retrieveleavedetails/<int:applicant_id>/',RetrieveSingleLeaveDetailView.as_view(),name='single_leave_detail'),
    path('acceptleave/<int:leave_id>/',LeaveAcceptingView.as_view(),name='accept_leave'),
    path('declineleave/<int:leave_id>/',LeaveDecliningView.as_view(),name='decline_leave'),
    
]
