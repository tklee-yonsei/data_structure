import unittest
from abc import ABC, abstractmethod

from data_structure.ds.interface.data_structure import DataStructure


class BaseDataStructureTest(ABC, unittest.TestCase):
    """모든 데이터 구조 테스트 클래스가 상속할 기본 클래스"""

    @abstractmethod
    def create_ds_instance(self) -> DataStructure:
        """
        자료구조 인스턴스를 생성하여 반환합니다.

        Returns
        -------
        object
            테스트할 자료구조의 인스턴스
        """
        pass
