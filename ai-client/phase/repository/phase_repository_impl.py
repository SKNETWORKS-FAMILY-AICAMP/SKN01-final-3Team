import os
import re

from phase.repository.phase_repository import PhaseRepository


class PhaseRepositoryImpl(PhaseRepository):
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

    def get_current_phase(self, *args, **kwargs):
        user_token, project_name = args
        phase_log_path = os.path.join("si_agent", "WareHouse", user_token, project_name, "logs", "Phase.log")
        
        if not os.path.exists(phase_log_path):
            return "operate si agent first."
        
        with open(phase_log_path, 'r') as f:
            phases = f.read()
        pattern = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\] - \[.*? file line:\d+\] - INFO:'
        phases = re.split(pattern, phases)
        
        if phases[0] == '':
            phases = phases[1:]
            
        cur_phase = phases[-1].strip()
        
        return cur_phase
    
    def get_backlogs(self, *args, **kwargs):
        user_token, project_name = args
        return """
    **Backlog 1: Basic Calculator Operations**

* Define the following basic calculator operations:
        + Addition
        + Subtraction
        + Multiplication
        + Division
        + Modulus (remainder)
* Implement the calculator to perform these operations on integers and floating-point numbers

**Backlog 2: Advanced Calculator Operations**

* Define the following advanced calculator operations:
        + Exponentiation
        + Square root
        + Logarithm
        + Trigonometric functions (sin, cos, tan)
* Implement the calculator to perform these operations on integers and floating-point numbers

**Backlog 3: Command-Line Interface (CLI)**

* Develop a command-line interface for the calculator that allows users to input calculations using text commands (e.g. "2 + 3" 
or "/ 4")
* Implement a parser to handle syntax errors and invalid inputs
* Allow users to save and load calculations from files

**Backlog 4: Graphical User Interface (GUI)**

* Develop a graphical user interface for the calculator that allows users to input calculations using buttons and text fields
* Implement a layout system to arrange the GUI elements in a visually appealing way
* Use a library like Tkinter or PyQt to create the GUI

**Backlog 5: Error Handling**

* Develop a robust error handling system that catches and handles exceptions raised during calculation operations
* Implement error messages that provide useful information about the cause of the error
* Allow users to retry calculations with a new input

**Backlog 6: Unit Tests**

* Write unit tests for individual calculator functions to ensure they are working correctly
* Use a testing framework like Pytest or Unittest to write and run tests
    """
    
    def get_test_reports(self, *args, **kwargs):
        user_token, project_name = args
        test_reports_log_path = os.path.join("si_agent", "WareHouse", user_token, project_name, "logs", "test_reports.log")
        
        if not os.path.exists(test_reports_log_path):
            return "operate si agent first."

        with open(test_reports_log_path, 'r') as file:
            log_content = file.read()

        pattern = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\] - \[.*? file line:\d+\] - INFO:'
        test_reports = re.split(pattern, log_content)

        if test_reports[0] == '':
            test_reports = test_reports[1:]

        return test_reports

    def get_code_reviews(self, *args, **kwargs):
        user_token, project_name = args
        code_review_log_path = os.path.join("si_agent", "WareHouse", user_token, project_name, "logs", "CodeReviewComment.log")
        
        if not os.path.exists(code_review_log_path):
            return "operate si agent first."

        with open(code_review_log_path, 'r') as file:
            log_content = file.read()

        pattern = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\] - \[.*? file line:\d+\] - INFO:'
        code_reviews = re.split(pattern, log_content)

        if code_reviews[0] == '':
            code_reviews = code_reviews[1:]

        return code_reviews