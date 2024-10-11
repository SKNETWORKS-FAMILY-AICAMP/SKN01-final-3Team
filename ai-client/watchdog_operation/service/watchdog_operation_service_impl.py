from watchdog_operation.repository.watchdog_operation_repository_impl import WatchdogOperationRepositoryImpl
from watchdog_operation.service.watchdog_operation_service import WatchdogOperationService


class WatchdogOperationServiceImpl(WatchdogOperationService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__watchdogOperationRepository = WatchdogOperationRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def operateWatchdog(self, *args, **kwargs):
        self.__watchdogOperationRepository.operate(*args, **kwargs)
        return {
            "status": "running"
        }
