from typing import TypeVar, Callable, Iterator, Tuple

KI = TypeVar('KI')
VI = TypeVar('VI')

KO = TypeVar('KO')
VO = TypeVar('VO')


class IteratorUtil(object):
    @staticmethod
    def filter(l: Iterator[VI], func: Callable[[VI], bool]) -> Iterator[VI]:
        for v in l:
            if func(v):
                yield v

    @staticmethod
    def map(l: Iterator[VI], func: Callable[[VI], VO]) -> Iterator[VO]:
        for v in l:
            yield func(v)

    @staticmethod
    def filter_pairs(l: Iterator[Tuple[KI, VI]], func: Callable[[KI, VI], bool]) -> Iterator[Tuple[KI, VI]]:
        for k, v in l:
            if func(k, v):
                yield (k, v)

    @staticmethod
    def map_pairs(l: Iterator[Tuple[KI, VI]], func: Callable[[KI, VI], VO]) -> Iterator[VO]:
        for k, v in l:
            yield func(k, v)
