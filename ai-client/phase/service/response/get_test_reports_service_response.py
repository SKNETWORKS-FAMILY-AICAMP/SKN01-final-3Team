from user_defined_protocol.protocol import UserDefinedProtocolNumber


class GetTestReportsResponse:
    def __init__(self, responseData):
        self.protocolNumber = UserDefinedProtocolNumber.GET_TEST_REPORTS.value

        for key, value in responseData.items():
            setattr(self, key, value)

    @classmethod
    def fromResponse(cls, responseData):
        return cls(responseData)

    def toDictionary(self):
        return self.__dict__

    def __str__(self):
        return f"GetTestReportsResponse({self.__dict__})"