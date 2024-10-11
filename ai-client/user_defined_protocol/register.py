import os
import sys

from first_user_defined_function_domain.service.fudf_service_impl import FudfServiceImpl
from first_user_defined_function_domain.service.request.fudf_just_for_test_request import FudfJustForTestRequest
from first_user_defined_function_domain.service.response.fudf_just_for_test_response import FudfJustForTestResponse
from multiple_user_test_point.service.multiple_user_test_point_service_impl import MultipleUserTestPointServiceImpl
from multiple_user_test_point.service.request.user_test_point_request import UserTestPointRequest
from multiple_user_test_point.service.response.user_test_point_response import UserTestPointResponse
from si_operation.service.si_operation_service_impl import SIOperationServiceImpl
from si_operation.service.request.si_operation_request import SIOperationRequest
from si_operation.service.response.si_operation_response import SIOperationResponse
from si_operation.service.request.get_file_list_request import GetFileListRequest
from si_operation.service.response.get_file_list_response import GetFileListResponse
from watchdog_operation.service.watchdog_operation_service_impl import WatchdogOperationServiceImpl
from watchdog_operation.service.request.watchdog_service_request import WatchdogOperationRequest
from watchdog_operation.service.response.watchdog_service_response import WatchdogOperationResponse
from phase.service.phase_service_impl import PhaseServiceImpl
from phase.service.request.get_current_phase_service_request import GetCurrentPhaseRequest
from phase.service.response.get_current_phase_service_response import GetCurrentPhaseResponse
from phase.service.request.get_backlogs_service_request import GetBacklogsRequest
from phase.service.response.get_backlogs_service_response import GetBacklogsResponse
from phase.service.request.get_test_reports_service_request import GetTestReportsRequest
from phase.service.response.get_test_reports_service_response import GetTestReportsResponse
from phase.service.request.get_code_review_service_request import GetCodeReviewsRequest
from phase.service.response.get_code_review_service_response import GetCodeReviewsResponse
from gpu_management.service.gpu_management_service_impl import GPUManagementServiceImpl
from gpu_management.service.response.gpu_management_response import GPUManagementResponse
from gpu_management.service.request.gpu_management_request import GPUManagementRequest

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'si_agent'))

from template.custom_protocol.service.custom_protocol_service_impl import CustomProtocolServiceImpl
from template.request_generator.request_class_map import RequestClassMap
from template.response_generator.response_class_map import ResponseClassMap

from user_defined_protocol.protocol import UserDefinedProtocolNumber


class UserDefinedProtocolRegister:
    @staticmethod
    def registerUserTestPointProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        multipleUserTestPointService = MultipleUserTestPointServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.USER_TEST_POINT,
            UserTestPointRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.USER_TEST_POINT,
            UserTestPointResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.USER_TEST_POINT,
            multipleUserTestPointService.operateUserTestPoint
        )

    @staticmethod
    def registerFirstUserDefinedProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        firstUserDefinedFunctionService = FudfServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            FudfJustForTestRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            FudfJustForTestResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.FIRST_USER_DEFINED_FUNCTION_FOR_TEST,
            firstUserDefinedFunctionService.justForTest
        )

    @staticmethod
    def registerSIAgentOperationProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        siAgentOperationService = SIOperationServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.SI_AGENT_OPERATION,
            SIOperationRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.SI_AGENT_OPERATION,
            SIOperationResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.SI_AGENT_OPERATION,
            siAgentOperationService.operateSIAgent
        )
        
        
    @staticmethod
    def registerWatchdogOperationProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        watchdogOperationService = WatchdogOperationServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.WATCHDOG_OPERATON,
            WatchdogOperationRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.WATCHDOG_OPERATON,
            WatchdogOperationResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.WATCHDOG_OPERATON,
            watchdogOperationService.operateWatchdog
        )
        
        
    @staticmethod
    def registerGetCurrentPhaseProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        phaseService = PhaseServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.GET_CURRENT_PHASE,
            GetCurrentPhaseRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.GET_CURRENT_PHASE,
            GetCurrentPhaseResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.GET_CURRENT_PHASE,
            phaseService.get_current_phase
        )
        
        
    @staticmethod
    def registerGetBacklogsProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        phaseService = PhaseServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.GET_BACKLOGS,
            GetBacklogsRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.GET_BACKLOGS,
            GetBacklogsResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.GET_BACKLOGS,
            phaseService.get_backlogs
        )

    @staticmethod
    def registerGetFileListProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        SIOperationService = SIOperationServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.GET_FILE_LIST,
            GetFileListRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.GET_FILE_LIST,
            GetFileListResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.GET_FILE_LIST,
            SIOperationService.get_file_list
        )

    @staticmethod
    def registerGetGPUstatusProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        GPUManagementService = GPUManagementServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.GET_GPU_STATUS,
            GPUManagementRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.GET_GPU_STATUS,
            GPUManagementResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.GET_GPU_STATUS,
            GPUManagementService.check_available
        )
        
    @staticmethod
    def registerGetTestReportsProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        phaseService = PhaseServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.GET_TEST_REPORTS,
            GetTestReportsRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.GET_TEST_REPORTS,
            GetTestReportsResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.GET_TEST_REPORTS,
            phaseService.get_test_reports
        )
        
    @staticmethod
    def registerGetCodeReviewsProtocol():
        customProtocolService = CustomProtocolServiceImpl.getInstance()
        phaseService = PhaseServiceImpl.getInstance()

        requestClassMapInstance = RequestClassMap.getInstance()
        requestClassMapInstance.addRequestClass(
            UserDefinedProtocolNumber.GET_CODE_REVIEW,
            GetCodeReviewsRequest
        )

        responseClassMapInstance = ResponseClassMap.getInstance()
        responseClassMapInstance.addResponseClass(
            UserDefinedProtocolNumber.GET_CODE_REVIEW,
            GetCodeReviewsResponse
        )

        customProtocolService.registerCustomProtocol(
            UserDefinedProtocolNumber.GET_CODE_REVIEW,
            phaseService.get_code_reviews
        )

    @staticmethod
    def registerUserDefinedProtocol():
        UserDefinedProtocolRegister.registerFirstUserDefinedProtocol()
        UserDefinedProtocolRegister.registerSIAgentOperationProtocol()
        UserDefinedProtocolRegister.registerWatchdogOperationProtocol()
        UserDefinedProtocolRegister.registerGetCurrentPhaseProtocol()
        UserDefinedProtocolRegister.registerGetBacklogsProtocol()
        UserDefinedProtocolRegister.registerGetFileListProtocol()
        UserDefinedProtocolRegister.registerGetGPUstatusProtocol()
        UserDefinedProtocolRegister.registerGetTestReportsProtocol()
        UserDefinedProtocolRegister.registerGetCodeReviewsProtocol()
        UserDefinedProtocolRegister.registerUserTestPointProtocol()
