from watchdog_operation.repository.watchdog_operation_repository import WatchdogOperationRepository
from watchdog_operation.entity.agent_watchdog import Watchdog


class WatchdogOperationRepositoryImpl(WatchdogOperationRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def operate(self, *args, **kwargs):
        watchdog = Watchdog("si_agent/WareHouse")
        watchdog.run()