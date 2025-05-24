from abc import ABC, abstractmethod
from typing import Optional, List

class DAO(ABC):

    @abstractmethod
    def get(self, id: int):
        """Busca ApiObject pelo id."""
        pass

    @abstractmethod
    def add(self, obj) -> None:
        """Adiciona um ApiObject."""
        pass

    @abstractmethod
    def update(self, obj) -> None:
        """Atualiza um ApiObject existente."""
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        """Remove ApiObject pelo id."""
        pass

    @abstractmethod
    def list_all(self):
        """Lista todos ApiObjects."""
        pass
