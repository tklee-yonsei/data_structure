import unittest

from data_structure.ds.hash_table import HashTable
from tests.ds.interface.base_test_addable import _BaseAddableTest
from tests.ds.interface.base_test_removable import _BaseRemovableTest


class TestHashTable(
    _BaseAddableTest,
    _BaseRemovableTest,
    unittest.TestCase,
):
    """HashTable에 대한 테스트 클래스."""

    def create_ds_instance(self):
        """HashTable 인스턴스를 생성하여 반환합니다."""
        return HashTable()


if __name__ == "__main__":
    unittest.main()
