from abc import ABC, abstractmethod


class WatchdogOperationRepository(ABC):
    @abstractmethod
    def operate(self, *args, **kwargs):
        pass
