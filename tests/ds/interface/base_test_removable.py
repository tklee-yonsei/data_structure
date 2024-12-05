from tests.ds.interface.base_test_data_structure import BaseDataStructureTest


class BaseRemovableTest(BaseDataStructureTest):
    """요소 삭제 테스트 베이스 클래스."""

    def setUp(self):
        """테스트 초기화: 공통 요소 배열 설정."""
        self.elements = [10, 20, 30, 40, 50]

    def test_remove_elements(self):
        """
        요소 삭제 후 검색되지 않는지 테스트.

        주어진 요소들을 추가한 후, 각각 삭제한 후 존재 여부를 확인합니다.
        """
        ds = self.create_ds_instance()
        for element in self.elements:
            ds.add(element)

        for element in self.elements:
            with self.subTest(element=element):
                self.assertTrue(
                    ds.remove(element),
                    f"Element {element} should be removable",
                )
                self.assertFalse(
                    ds.search(element),
                    f"Element {element} should not be found after removal",
                )

    def test_remove_non_existing_element(self):
        """
        존재하지 않는 요소를 삭제 시도하는 테스트.

        존재하지 않는 요소를 삭제할 때 False를 반환하는지 확인합니다.
        """
        ds = self.create_ds_instance()
        non_existing_element = 60
        self.assertFalse(
            ds.remove(non_existing_element),
            "Removing non-existing element should return False",
        )
