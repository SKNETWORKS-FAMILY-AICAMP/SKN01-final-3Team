from abc import ABC, abstractmethod


class GPUManagementRepository(ABC):
    @abstractmethod
    def check_available(self, *args, **kwargs):
        pass
