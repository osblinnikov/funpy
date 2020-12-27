import logging
from typing import TypeVar, Callable, Iterator, Dict, Generic, Tuple

from funpy.iteratorutil import IteratorUtil

KI = TypeVar('KI')
VI = TypeVar('VI')

KO = TypeVar('KO')
VO = TypeVar('VO')


class FunDict(Generic[KI, VI]):
    def __init__(self, d: Dict[KI, VI]=None):
        if d is None:
            d = dict()
        self.d = d
    	if not isinstance(self.d, dict):
	    self.d = dict(self.d)

    def py(self) -> Dict[KI, VI]:
        return self.d

    def py_iter(self) -> Iterator[Tuple[KI, VI]]:
        for k, v in self.d.items():
            yield (k, v)

    def to_list(self) -> 'FunList[Tuple[KI, VI]]':
        from collection.funlist import FunList
        return FunList(self.py_iter())

    def map(self, func: Callable[[KI, VI], Tuple[KO, VO]]) -> 'FunDict[KO, VO]':
        return FunDict(dict(IteratorUtil.map_pairs(self.py_iter(), func)))

    def map_to_list(self, func: Callable[[KI, VI], VO]) -> 'FunList[VO]':
        from collection.funlist import FunList
        return FunList(IteratorUtil.map_pairs(self.py_iter(), func))

    def filter(self, func: Callable[[KI, VI], bool]) -> 'FunDict[KI, VI]':
        return FunDict(dict(IteratorUtil.filter_pairs(self.py_iter(), func)))

    def find(self, func: Callable[[KI, VI], bool]) -> (KI, VI):
        return next(IteratorUtil.filter_pairs(self.py_iter(), func), None)

    def __str__(self):
        return str(self.py())

    def print(self, msg="") -> 'FunDict[KI, VI]':
        logging.getLogger(self.__class__.__name__).info("%s %s", msg, self.__str__())
        return self

    def count(self):
        return len(self.py())
