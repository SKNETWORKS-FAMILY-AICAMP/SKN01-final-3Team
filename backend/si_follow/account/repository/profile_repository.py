from abc import ABC, abstractmethod


class ProfileRepository(ABC):

    @abstractmethod
    def create(self, email, account):
        pass

