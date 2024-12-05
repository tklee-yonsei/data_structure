from abc import ABC, abstractmethod


class Addable(ABC):
    """요소를 추가하는 인터페이스 클래스."""

    @abstractmethod
    def add(self, value):
        """
        주어진 값을 추가합니다.

        Parameters
        ----------
        value : object
            추가할 값입니다.
        """
        pass
