from abc import ABC, abstractmethod


class PhaseRepository(ABC):
    @abstractmethod
    def get_current_phase(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def get_backlogs(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def get_test_reports(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def get_code_reviews(self, *args, **kwargs):
        pass
