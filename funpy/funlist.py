import logging
from typing import TypeVar, Callable, List, Iterator, Generic, Tuple

from funpy.iteratorutil import IteratorUtil

I = TypeVar('I')
O = TypeVar('O')

KO = TypeVar('KO')
VO = TypeVar('VO')


class FunList(Generic[I]):
    def __init__(self, l: Iterator[I]=None):
        if l is None:
            l = list()
        self.l = l

    def py(self) -> List[I]:
        if not isinstance(self.l, list):
            self.l = list(self.l)
        return self.l

    def py_iter(self) -> Iterator[I]:
        return self.l

    def zip_with_index(self) -> 'FunList[(int, I)]':
        return FunList(enumerate(self.l))

    def zip(self, right: 'FunList[O]') -> 'FunList[(I, O)]':
        return FunList(zip(self.py(), right.py()))

    def map(self, func: Callable[[I], O]) -> 'FunList[O]':
        return FunList(list(IteratorUtil.map(self.l, func)))

    def map_to_dict(self, func: Callable[[I], Tuple[KO, VO]]) -> 'FunDict[KO, VO]':
        from collection.fundict import FunDict
        return FunDict(dict(IteratorUtil.map(self.l, func)))

    def map_pair(self, func: Callable[[Tuple[KO, VO]], O]) -> 'FunList[O]':
        return FunList(list(IteratorUtil.map_pairs(self.l, func)))

    def filter(self, func: Callable[[I], bool]) -> 'FunList[I]':
        return FunList(list(IteratorUtil.filter(self.l, func)))

    def find(self, func: Callable[[I], bool]) -> I:
        return next(IteratorUtil.filter(self.l, func), None)

    def __str__(self):
        return str(self.py())

    def print(self, msg="") -> 'FunList[I]':
        logging.getLogger(self.__class__.__name__).info("%s %s", msg, self.__str__())
        return self

    def count(self):
        return len(self.py())

    def sum(self):
        return sum(self.py())
