from django.test import TestCase

import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Users
from .serializers import UsersSerializer

client = Client()


class AllUsersTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            'username': 'James',
            'roles': 'purchaser'
        }
        self.invalid_payload = [
            {
                'username': '',
                'roles': 'purchaser'},
            {
                'username': 'James',
                'roles': ''
            }
        ]

    def test_get_all_users(self):
        response = client.get(reverse(viewname='get_post_all_users'))
        # get data from db
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_user(self):
        response = client.post(
            reverse('get_post_all_users'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = client.post(
            reverse('get_post_all_users'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserDetailTest(TestCase):

    def setUp(self):
        self.liza = Users.objects.create(
            username='Liza', roles='manager')

        self.blake = Users.objects.create(
            name='Blake', roles='[programmer,purchaser]')

    def test_valid_update_puppy(self):
        response = client.put(
            reverse('get_put_delete_user', kwargs={'pk': self.liza.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_puppy(self):
        response = client.put(
            reverse('get_put_delete_user', kwargs={'pk': self.blake.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
