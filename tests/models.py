from django.db import models
from ndarray.fields import NDArrayField


class Model(models.Model):
    ar = NDArrayField(null=True)
