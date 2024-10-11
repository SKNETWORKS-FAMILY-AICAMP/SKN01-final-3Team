from abc import ABC, abstractmethod


class SIOperationRepository(ABC):
    @abstractmethod
    def operate(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def get_file_list(self, *args, **kwargs):
        pass
