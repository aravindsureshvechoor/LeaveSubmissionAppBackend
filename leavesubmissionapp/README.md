# LeaveSubmissionAppBackend

The name of the project is Leavesubmissionapp

There are two apps:
	1.Authentication
	2.Leavemanagement
	
	1.Authentication
	Registration of Manager and Employee is done,
	When signing up,user can select his role and seperate LOGIN has done for both Manager and Employee
	
	2.Leavemanagement
	This app deals with api's which helps the Employee to submit a leave and also the Manager to accept or decline it respectievely.
	Other api's are also added to fetch the details of each employee and his leaves.
	
Test Cases
Test Cases are written on both apps , test cases for urls and views have been written


How to Use:

command to start backend : python manage.py runserver
command to start frontend : npm start
command to run testcases : python manage.py test

After runnign both the Django App and React App, 
User is directed to the landing page which is the login page for EMPLOYEE,
From their ,if the user is a manager, he can move to the manager login page else if the user wants to register , he can move to the signup part

After authentication, with respect to their roles, Manager can accept or decline the Employees leave request and Employee can submit a new leave request ,plus he can see all his previous leave requests and their status.




Technologies Used:

Backend - Django Rest Frameword, JWT 
Frontend - React JS, Redux Toolkit
