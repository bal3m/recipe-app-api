from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def teat_create_user_with_email_successful(self):
        """Test creating user with an email is successful"""
        email='bal3m@bal3m.com'
        password='bal3m123'
        user= get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    def test_new_user_email_normalized(self):
        """Test the email for new user is normalized"""
        email= 'test@BAL3M.COM'
        user= get_user_model().objects.create_user(email, 'test1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None)
    
    def test_create_new_superuser(self):
        """Creating new superuser"""
        user= get_user_model().objects.create_superuser(
            'test@bal3m.com',
            'test1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)