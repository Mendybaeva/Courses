from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import *

# tests for all of project
# write comments for reviewer


class ModelsTestCase(TestCase):

    def setUp(self):
        self.course_name = 'english courses'
        self.course = Course(name=self.course_name,)
        self.category_name = 'language courses'
        self.category = Category(name=self.category_name)

    def test_model_create_category(self):
        old_count = Category.objects.count()
        self.category.save()
        new_count = Category.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_create_course(self):
        old_count = Course.objects.count()
        self.course.save()
        new_count = Course.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_readable_representation(self):
        self.assertEqual(str(self.course), self.course_name)
        self.assertEqual(str(self.category), self.category_name)


class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.courses_data = {
                                "name": "Мелодия",
                                "description": "Курсы по изучению такта и музыки",
                                "category":'',
                                "logo": "Music",
                                "contacts": [
                                    {
                                        "type": 1,
                                        "value": "0702584685"
                                    }
                                ],
                                "branches": [
                                    {
                                        "latitude": "741258963",
                                        "longitude": "987456321",
                                        "address": "г.Бишкек пр.Чуй 34"
                                    }
                                ]
                            }
        self.category_data = {
                                "name": "Курсы рисования",
                                "imgpath": "/pictures/2.jpg"
                            }
        self.response_course = self.client.post(
            reverse('create'),
            self.courses_data,
        )
        self.response_category = self.client.post(
            reverse('category'),
            self.category_data,
        )

    def test_api_create_course(self):
        self.assertEqual(self.response_course.status_code, status.HTTP_201_CREATED)

    def test_api_create_category(self):
        self.assertEqual(self.response_category.status_code, status.HTTP_201_CREATED)

    def test_api_get_course(self):
        try:
            course = Course.objects.get(id=1)
            response = self.client.get(
                '/courses/',
                kwargs={'pk': course.id}
            )
        except Course.DoesNotExist:
            return 'Course does not exist'
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, course)

    def test_api_get_category(self):
        try:
            category = Category.objects.get(id=1)
            response = self.client.get(
                '/category/',
                kwargs={'pk': category.id}
            )
        except Category.DoesNotExist:
            return 'Category does not exist'
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, category)
