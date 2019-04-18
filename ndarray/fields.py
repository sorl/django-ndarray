import numpy as np
import pickle
from django.core import checks
from django.db import models
from django.utils.translation import gettext_lazy as _


class NDArrayField(models.BinaryField):
    description = _('NDArray field')
    empty_values = [None, np.array([])]

    def check(self, **kwargs):
        return [*super().check(**kwargs), *self._check_default_value()]

    def _check_default_value(self):
        if self.has_default() and not isinstance(self.default, np.ndarray):
            return [checks.Error("NDArrayField's defaults must be an ndarray", obj=self)]
        return []

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is not None:
            return value.dumps()

    def from_db_value(self, value, expression, connection):
        if value is not None:
            return pickle.loads(value)

    def deconstruct(self):
        return models.BinaryField().deconstruct()
