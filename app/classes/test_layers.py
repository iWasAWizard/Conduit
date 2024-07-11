#!/bin/python
import json
import xml.etree.ElementTree as ET
from typing import List, Dict


class TestStep:
    def __init__(self, step_id: int, message: str):
        self.step_id = step_id
        self.message = message
        self.result = None

    def execute(self):
        # Placeholder for test step execution logic
        # Arrange, Act, Assert
        print(f"Executing step {self.step_id}: {self.message}")
        self.result = "pass"  # This should be replaced with actual result

    def verify(self):
        print(f"Validating step {self.step_id}: {self.message}")

    def to_dict(self):
        return {
            'step_id': self.step_id,
            'message': self.message,
            'result': self.result
        }


class TestCase:
    def __init__(self, case_id: int, description: str):
        self.case_id = case_id
        self.description = description
        self.steps: List[TestStep] = []
        self.result = None

    def add_step(self, step: TestStep):
        self.steps.append(step)

    def execute(self):
        print(f"Executing test case {self.case_id}: {self.description}")
        for step in self.steps:
            step.execute()
        self.result = all(step.result == "pass" for step in self.steps)

    def verify(self):
        pass

    def to_dict(self):
        return {
            'case_id': self.case_id,
            'description': self.description,
            'result': self.result,
            'steps': [step.to_dict() for step in self.steps]
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    def to_xml(self):
        testcase = ET.Element('testcase', attrib={'id': str(self.case_id), 'description': self.description,
                                                  'result': str(self.result)})
        for step in self.steps:
            step_elem = ET.SubElement(testcase, 'teststep',
                                      attrib={'id': str(step.step_id), 'message': step.message, 'result': step.result})
        return ET.tostring(testcase, encoding='unicode')


class TestCampaign:
    def __init__(self, campaign_id: int, description: str):
        self.campaign_id = campaign_id
        self.description = description
        self.test_cases: List[TestCase] = []

    def add_test_case(self, test_case: TestCase):
        self.test_cases.append(test_case)

    def execute(self):
        print(f"Executing test campaign {self.campaign_id}: {self.description}")
        for test_case in self.test_cases:
            test_case.execute()

    def to_dict(self):
        return {
            'campaign_id': self.campaign_id,
            'description': self.description,
            'test_cases': [test_case.to_dict() for test_case in self.test_cases]
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

    def to_xml(self):
        campaign = ET.Element('testcampaign', attrib={'id': str(self.campaign_id), 'description': self.description})
        for test_case in self.test_cases:
            case_elem = ET.SubElement(campaign, 'testcase', attrib={'id': str(test_case.case_id), 'description': test_case.description, 'result': str(test_case.result)})
            for step in test_case.steps:
                step_elem = ET.SubElement(case_elem, 'teststep', attrib={'id': str(step.step_id), 'message': step.message, 'result': step.result})
        return ET.tostring(campaign, encoding='unicode')

    def to_html(self):
        html = f"<html><body><h1>Test Campaign {self.campaign_id}</h1><p>{self.description}</p>"
        for test_case in self.test_cases:
            html += f"<h2>Test Case {test_case.case_id}</h2><p>{test_case.description}</p><table border='1'><tr><th>Step ID</th><th>Message</th><th>Result</th></tr>"
            for step in test_case.steps:
                html += f"<tr><td>{step.step_id}</td><td>{step.message}</td><td>{step.result}</td></tr>"
            html += f"</table><p>Overall Result: {test_case.result}</p>"
        html += "</body></html>"
        return html
