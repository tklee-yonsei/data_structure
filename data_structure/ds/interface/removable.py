from abc import ABC, abstractmethod


class Removable(ABC):
    """요소를 삭제하는 인터페이스 클래스."""

    @abstractmethod
    def remove(self, value):
        """
        주어진 값을 삭제합니다.

        Parameters
        ----------
        value : object
            삭제할 값입니다.

        Returns
        -------
        bool
            값이 존재하여 삭제된 경우 True, 그렇지 않으면 False를 반환합니다.
        """
        pass
