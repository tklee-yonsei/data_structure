from tests.ds.interface.base_test_data_structure import BaseDataStructureTest


class BaseAddableTest(BaseDataStructureTest):
    """요소 추가 테스트 베이스 클래스."""

    def setUp(self):
        """테스트 초기화: 공통 요소 배열 설정."""
        self.elements = [10, 20, 30, 40, 50]

    def test_add_elements(self):
        """
        요소 추가 후 검색이 가능한지 테스트.

        주어진 요소들을 추가한 후, 각각이 존재하는지 확인합니다.
        """
        ds = self.create_ds_instance()
        for element in self.elements:
            ds.add(element)
        for element in self.elements:
            with self.subTest(element=element):
                self.assertTrue(
                    ds.search(element),
                    f"Element {element} should be present after addition",
                )
