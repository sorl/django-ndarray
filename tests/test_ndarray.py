import numpy as np
from django.test import TestCase
from .models import Model


class TestNdarray(TestCase):
    def test_null(self):
        obj = Model.objects.create(ar=None)
        obj = Model.objects.get(pk=obj.pk)
        self.assertEqual(obj.ar, None)

    def test_array_type(self):
        ar = np.array([])
        obj = Model.objects.create(ar=ar)
        obj = Model.objects.get(pk=obj.pk)
        self.assertTrue(isinstance(obj.ar, np.ndarray))

    def test_vector(self):
        ar = np.array([1, 2, 3])
        obj = Model.objects.create(ar=ar)
        obj = Model.objects.get(pk=obj.pk)
        self.assertTrue((obj.ar == ar).all())

    def test_matrix(self):
        ar = np.array([[1, 2, 3], [4, 5, 6]])
        obj = Model.objects.create(ar=ar)
        obj = Model.objects.get(pk=obj.pk)
        self.assertTrue((obj.ar == ar).all())
