import abc
from allocation.domain import model
from allocation.adapters import orm

# Here. the abstract classes are used to better explain what the interface of the repository abstraction is

class AbstractRepository(abc.ABC):
    @abc.abstractmethod # What makes ABCs actually "work" in Python
    def add(self, batch: model.Batch):
        raise NotImplementedError
        
    @abc.abstractmethod
    def get(self, reference) -> model.Batch:
        raise NotImplementedError