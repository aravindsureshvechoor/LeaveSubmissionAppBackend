from django.urls import path
from .views import LeaveSubmissionView,RetrieveLeaveDetailsView
urlpatterns = [
    path('leavesubmission/',LeaveSubmissionView.as_view(),name='leave_submission'),
    path('retrievallleavedetails/',RetrieveLeaveDetailsView.as_view(),name='leave_details')
]
