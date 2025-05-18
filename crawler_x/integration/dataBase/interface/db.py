from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    
    @abstractmethod
    def execute(self, query: str, params: tuple = ()):
        pass

    @abstractmethod
    def insert(self, table: str, data: dict) -> int:
        pass

    @abstractmethod
    def update(self, table: str, data: dict, condition: str, params: tuple = ()):
        pass

    @abstractmethod
    def delete(self, table: str, condition: str, params: tuple = ()):
        pass