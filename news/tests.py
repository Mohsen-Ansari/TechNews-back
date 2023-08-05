from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import News, Reference, Tag


class NewsViewTestCase(TestCase):
    def setUp(self):
        # Create a test client
        self.client = APIClient()

        # Create test data
        self.tag1 = Tag.objects.create(name='Tag 1')
        self.tag2 = Tag.objects.create(name='Tag 2')

        self.reference1 = Reference.objects.create(name='Reference 1', author='test name one', date='2022-04-25')
        self.reference2 = Reference.objects.create(name='Reference 2', author='test name two', date='2015-08-12')

        self.news1 = News.objects.create(title='News 1', content='Content 1')
        self.news1.tags.add(self.tag1, self.tag2)
        self.news1.references.add(self.reference1, self.reference2)

        self.news2 = News.objects.create(title='News 2', content='Content 2')
        self.news2.tags.add(self.tag1)
        self.news2.references.add(self.reference1)

    def test_get_news(self):
        response = self.client.get('/api/news/get/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
