from abc import ABC

from data_structure.ds.interface.addable import Addable
from data_structure.ds.interface.removable import Removable


class DataStructure(Addable, Removable, ABC):
    """데이터 구조의 인터페이스."""

    pass
