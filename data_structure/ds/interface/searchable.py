from abc import ABC, abstractmethod


class Searchable(ABC):
    """요소를 검색하는 인터페이스 클래스."""

    @abstractmethod
    def search(self, value):
        """
        주어진 값을 검색합니다.

        Parameters
        ----------
        value : object
            검색할 값입니다.

        Returns
        -------
        bool
            값이 존재하면 True, 없으면 False를 반환합니다.
        """
        pass
