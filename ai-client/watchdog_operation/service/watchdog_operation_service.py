from abc import ABC, abstractmethod


class WatchdogOperationService(ABC):
    @abstractmethod
    def operateWatchdog(self, *args, **kwargs):
        pass
