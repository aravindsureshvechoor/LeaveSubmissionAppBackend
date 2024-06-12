from django.test import TestCase,Client
from Authentication.serializers import *
from django.urls import reverse
from django.contrib.auth import get_user_model
import json
User = get_user_model()

class UserRegistrationView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_user_registration_success(self):
        user_data = {
            'user_name':'sampleusername',
            'role':'manager',
            'email':'sampleuser@gmail.com',
            'password':'samplepassword',
            'confirm_password':'samplepassword',
        }

        serialized_data = UserRegistrationSerializer(data=user_data)

        self.assertTrue(serialized_data.is_valid())

        url = reverse('user_signup')

        response = self.client.post(url,data=user_data,format='json')

        self.assertEqual(response.status_code,201)

    # provides wrong data
    def test_user_registration_failure(self):
        user_data = {
            'first_name'       :'user_firstname',
            'last_name'        : 'user_lastname',
            'email'            : 'user@example.com',
            'password'         : 'userpassword',
            'confirm_password' : 'userpassword'
        }

        serialized_data        = UserRegistrationSerializer(data=user_data)

        self.assertFalse(serialized_data.is_valid())

        url                    = reverse('user_signup')

        response               = self.client.post(url,data=user_data,format='json')

        self.assertEqual(response.status_code,400)

# this class checks the genuinity of the UserLoginView
class TestUserLoginView(TestCase):
    
    def setUp(self):
        self.client = Client()

    # user with the correct credentials
    def test_user_login_success(self):

        test_user   = User.objects.create_user(

            user_name = 'sampleusername',
            role = 'manager',
            email = 'sampleuser@gmail.com',
            password = 'samplepassword',

                                           )

        login_data  = {
                'email'   :'sampleuser@gmail.com',
                'password':'samplepassword'
                     }

        url         = reverse('user_login')

        response    = self.client.post(url,data=login_data,format='json')

        self.assertEqual(response.status_code,200)
        self.assertIn('refresh', response.data['data'])
        self.assertIn('access', response.data['data'])
    


    # testcase with invalid credentials
    def test_user_login_success(self):

        test_user   = User.objects.create_user(

                    user_name = 'sampleusername',
                    role = 'manager',
                    email = 'sampleuser@gmail.com',
                    password = 'samplepassword',

                                           )

        login_data = {
                'email'   :'user@example.com',
                'password':'wrongpassword'
                     }

        url        = reverse('user_login')

        response   = self.client.post(url,data=login_data,format='json')

        self.assertEqual(response.status_code,401)