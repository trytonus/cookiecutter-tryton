# -*- coding: utf-8 -*-
"""
    tests/test_views_depends.py

    :copyright: (C) {{ cookiecutter.year }} by {{ cookiecutter.author }}
    :license: see LICENSE for more details.
"""
import unittest

import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class TestViewsDepends(ModuleTestCase):
    """Test View Depends."""
    module = '{{ cookiecutter.module_name }}'


def suite():
    """
    Define suite
    """
    test_suite = trytond.tests.test_tryton.suite()
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestViewsDepends)
    )
    return test_suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
