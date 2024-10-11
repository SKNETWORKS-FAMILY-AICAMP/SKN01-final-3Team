from gpu_management.repository.gpu_management_repository_impl import GPUManagementRepositoryImpl
from gpu_management.service.gpu_management_service import GPUManagementService


class GPUManagementServiceImpl(GPUManagementService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__gpuManagementRepository = GPUManagementRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def check_available(self, *args, **kwargs):
        api_url = args[0]
        status = self.__gpuManagementRepository.check_available(*args, **kwargs)
        return {
            "api_url": api_url,
            "status": status
        }
