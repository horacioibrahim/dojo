"""
Testes para buscador de OU no SEP
"""
from __future__ import absolute_import
import unittest
from types import FileType

from aggregate import load_file, check_exist, iterate, remove_pattern_name

class TestAggregate(unittest.TestCase):

    def test_load_file(self):
        filename = '../assets/localidades_mal_formadas.csv'
        f = load_file(filename)
        self.assertEqual(FileType, type(f))

    def test_iterate(self):
        filename = '../assets/localidades_mal_formadas.csv'
        f = load_file(filename)
        is_has = iterate(check_exist, 'EADI', f)
        self.assertTrue(is_has, msg='uppercase test')
        is_has = iterate(check_exist, 'eadi', f)
        self.assertTrue(is_has, msg='lowercase test')

    def test_remove_pattern_ou_name(self):
        removed = remove_pattern_name('RFB_EADI_SANTOS_MOROTA')
        self.assertEqual(list, type(removed))
        # check len of list. must be 2 (in case)
        self.assertEqual(2, len(removed))



if __name__ == '__name__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAggregate)
    unittest.TextTestRunner(verbosity=2).run(suite)
