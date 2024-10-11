from abc import ABC, abstractmethod


class SIOperationService(ABC):
    @abstractmethod
    def operateSIAgent(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def get_file_list(self, *args, **kwargs):
        pass
