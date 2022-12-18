from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import TestCase


class MatrixTests(APITestCase):
    def test1_matrix_correct(self):

        url = reverse(viewname='n_matrix')
        response = self.client.get(url, data={'size': 2, 'a': 2, 'matrix': '-1_-6*2_6'})
        self.assertEqual(response.data, {
            "size": 2,
            "matrix": [[-1.0, -6.0], [2.0, 6.0]],
            "mulMatrix": [[-2.0, -12.0], [4.0, 12.0]],
        })
