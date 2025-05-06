from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Policy
from datetime import date, timedelta

class PolicyAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.policy_data = {
            'customer_name': 'John Silva',
            'policy_type': 'auto',
            'expiry_date': (date.today() + timedelta(days=365)).isoformat()
        }
        self.policy = Policy.objects.create(
            customer_name='Maria Santos',
            policy_type='home',
            expiry_date=date.today() + timedelta(days=365)
        )

    def test_create_policy(self):
        response = self.client.post(reverse('policy-list'), self.policy_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Policy.objects.count(), 2)

    def test_get_policies_list(self):
        response = self.client.get(reverse('policy-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_policy_detail(self):
        response = self.client.get(reverse('policy-detail', kwargs={'pk': self.policy.policy_id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], 'Maria Santos')

    def test_update_policy(self):
        updated_data = self.policy_data.copy()
        updated_data['customer_name'] = 'John Silva Updated'
        response = self.client.put(
            reverse('policy-detail', kwargs={'pk': self.policy.policy_id}),
            updated_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.policy.refresh_from_db()
        self.assertEqual(self.policy.customer_name, 'John Silva Updated')

    def test_delete_policy(self):
        response = self.client.delete(reverse('policy-detail', kwargs={'pk': self.policy.policy_id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Policy.objects.count(), 0)

    def test_invalid_expiry_date(self):
        invalid_data = self.policy_data.copy()
        invalid_data['expiry_date'] = (date.today() - timedelta(days=1)).isoformat()
        response = self.client.post(reverse('policy-list'), invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
