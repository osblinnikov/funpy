from unittest import TestCase

from funpy.fundict import FunDict
from logging_config_for_tests import logging_config

logging_config()


class TestFunDict(TestCase):
    def test_fundict(self):
        def filter_gr_1(k: str, v: str) -> bool:
            return k != '3'

        d = FunDict({1: 2, 2: 3, 3: 4})
        res = (d
               .map(lambda k, v: (k + 1, v))
               .map(lambda k, v: (str(k), str(v)))
               .print("message1")
               .filter(lambda k, v: k != '2')
               .filter(filter_gr_1)
               .print("message2")
               .to_list()
               .py()
               )
        assert res == [('4', '4')]
