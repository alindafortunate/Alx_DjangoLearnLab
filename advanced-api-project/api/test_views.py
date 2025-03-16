from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from .models import Book, Author


class BookTest(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Introduction to Django",
            publication_year=2023,
            author=Author.objects.create(name="Alinda Fortunate"),
        )
        self.url = reverse("create-book")
    
    def test_create_book(self):
        """
        Test method to ensure that we can create a book
        """
        data = {
            "title": "Introduction to Django",
            "publication_year": 2023,
            "author": 1,
        }
        response = self.client.post(self.url, data)
        response = self.client.login()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Introduction to Django")
        
    # def test_get_book(self):
    #     """
    #     Test method to ensure that we list a book
    #     """

    #     response = self.client.get(self.url)
    #     self.assertEqual(response.status_code, 200)
    
