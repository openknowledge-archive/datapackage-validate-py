# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .schema import Schema
from .validate import validate
import warnings

warnings.warn(
    'The "datapackage-validate" package is deprecated. Please use '
    '"datapackage" instead',
    DeprecationWarning
)

__all__ = ['validate']
