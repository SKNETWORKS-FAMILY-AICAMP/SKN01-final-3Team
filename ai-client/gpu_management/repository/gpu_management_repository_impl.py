import requests

from gpu_management.repository.gpu_management_repository import GPUManagementRepository


class GPUManagementRepositoryImpl(GPUManagementRepository):
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

    def check_available(self, *args, **kwargs):
        api_url = args[0]
        status = False
        try:
            res = requests.get(api_url)
            if res.status_code == 200 and res.content.decode() == "Ollama is running":
                status = True
        except Exception as e:
            print(f"error occurred {e}")
        
        return status
