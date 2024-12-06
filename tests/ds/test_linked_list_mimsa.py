import unittest

from data_structure.ds.linked_list_mimsa import linked_list_mimsa
from tests.ds.interface.base_test_addable import _BaseAddableTest
from tests.ds.interface.base_test_removable import _BaseRemovableTest


class Testlinked_list_mimsa(
    _BaseAddableTest,
    _BaseRemovableTest,
    unittest.TestCase,
):
    """LinkedList에 대한 테스트 클래스."""

    def create_ds_instance(self):
        """LinkedList 인스턴스를 생성하여 반환합니다."""
        return linked_list_mimsa()


if __name__ == "__main__":
    unittest.main()
