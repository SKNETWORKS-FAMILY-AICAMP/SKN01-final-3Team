from abc import ABC, abstractmethod


class GPUManagementService(ABC):
    @abstractmethod
    def check_available(self, *args, **kwargs):
        pass
