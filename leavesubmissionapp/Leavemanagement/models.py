from django.db import models
from Authentication.models import AppUser

# Create your models here.
class LeaveApplication(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('annual', 'Annual'),
        ('sick', 'Sick'),
        ('vacation', 'Vacation'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('leave granted', 'Leave Granted'),
        ('leave declined', 'Leave Declined'),
    ]

    applicant = models.ForeignKey(AppUser,on_delete=models.CASCADE)
    type_of_leave = models.CharField(max_length=10, choices=LEAVE_TYPE_CHOICES)
    startdate = models.CharField(max_length=100)
    enddate = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.applicant.user_name} - {self.type_of_leave} from {self.startdate} to {self.enddate} ({self.status})"

