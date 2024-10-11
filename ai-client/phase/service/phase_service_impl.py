from phase.repository.phase_repository_impl import PhaseRepositoryImpl
from phase.service.phase_service import PhaseService


class PhaseServiceImpl(PhaseService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__phaseRepository = PhaseRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def get_current_phase(self, *args, **kwargs):
        current_phase = self.__phaseRepository.get_current_phase(*args, **kwargs)
        return {
            "user_token": args[0],
            "project_name": args[1],
            "phase": current_phase
        }
        
    def get_backlogs(self, *args, **kwargs):
        backlog = self.__phaseRepository.get_backlogs(*args, **kwargs)
        return {
            "user_token": args[0],
            "project_name": args[1],
            "backlog": backlog
        }
        
    def get_test_reports(self, *args, **kwargs):
        test_reports = self.__phaseRepository.get_test_reports(*args, **kwargs)
        return {
            "user_token": args[0],
            "project_name": args[1],
            "test_reports": test_reports
        }
        
    def get_code_reviews(self, *args, **kwargs):
        code_reviews = self.__phaseRepository.get_code_reviews(*args, **kwargs)
        return {
            "user_token": args[0],
            "project_name": args[1],
            "code_review": code_reviews
        }
        