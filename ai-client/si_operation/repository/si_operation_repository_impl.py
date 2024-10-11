from si_operation.repository.si_operation_repository import SIOperationRepository

import os
import sys
from glob import glob

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'si_agent'))

from si_agent.runner import Runner


class SIOperationRepositoryImpl(SIOperationRepository):
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
        ks = ['config', 'model_name', 'user_token', 'task', 'project', 'base_url']
        kwargs = {k:v for k, v in zip(ks, args)}
        runner = Runner()
        runner.run(**kwargs)
        
    def get_file_list(self, *args, **kwargs):
        ks = ['user_token', 'project_name']
        kwargs = {k:v for k, v in zip(ks, args)}
        target_dir = f"si_agent/WareHouse/{kwargs['user_token']}/{kwargs['project_name']}"
        file_list = glob(f"{target_dir}/**", recursive=True)
        return [f.split(target_dir + "/")[-1] for f in file_list]
