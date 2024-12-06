import unittest

from data_structure.ds.linked_list_pinesound import LinkedListpinesound
from tests.ds.interface.base_test_addable import _BaseAddableTest
from tests.ds.interface.base_test_removable import _BaseRemovableTest


class TestLinkedListpinesound(
    _BaseAddableTest,
    _BaseRemovableTest,
    unittest.TestCase,
):
    """LinkedListpinesound에 대한 테스트 클래스."""

    def create_ds_instance(self):
        """LinkedListpinesound 인스턴스를 생성하여 반환합니다."""
        return LinkedListpinesound()


if __name__ == "__main__":
    unittest.main()
