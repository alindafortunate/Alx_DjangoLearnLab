from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from .models import Book


class BookTest(APITestCase):
    def test_create_book(self):
        """
        Test method to ensure that we can create a book
        """
        url = reverse("create-book")
        data = {
            "title": "Introduction to Django",
            "publication_year": 2023,
            "author": 1,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
