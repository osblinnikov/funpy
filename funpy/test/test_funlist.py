from unittest import TestCase

from funpy.funlist import FunList
from logging_config_for_tests import logging_config

logging_config()


class TestFunList(TestCase):
    def test_funlist(self):
        def filter_gr_1(a: int) -> bool:
            return a > 1

        l = FunList([1, 2, 3])
        res = (l
               .map(lambda a: a + 2)
               .map(lambda a: a - 3)
               .filter(lambda a: a < 5)
               .filter(filter_gr_1)
               .print("message")
               .map_to_dict(lambda a: (a, a + 1))
               .py()
               )

        assert res == {2: 3}
