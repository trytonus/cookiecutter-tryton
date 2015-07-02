# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) {{ cookiecutter.year }} by {{ cookiecutter.author }}
    :license: see LICENSE for details.
"""
from trytond.pool import Pool


def register():
    Pool.register(
        module='{{ cookiecutter.module_name }}', type_='model'
    )
