#!/bin/python
import json
import xml.etree.ElementTree as ET


def case_to_html(self):
    html = f"<html><body><h1>Test Case {self.case_id}</h1><p>{self.description}</p><table border='1'><tr><th>Step ID</th><th>Message</th><th>Result</th></tr>"
    for step in self.steps:
        html += f"<tr><td>{step.step_id}</td><td>{step.message}</td><td>{step.result}</td></tr>"
    html += f"</table><p>Overall Result: {self.result}</p></body></html>"
    return html


def campaign_to_dict(self, campaign_id, description, test_cases):
    return {
        'campaign_id': self.campaign_id,
        'description': self.description,
        'test_cases': [test_case.to_dict() for test_case in self.test_cases]
    }


def campaign_to_json(self):
    return json.dumps(self.to_dict(), indent=4)


def campaign_to_xml(self, test_campaign_name):
    campaign = ET.Element('testcampaign', attrib={'id': str(self.campaign_id), 'description': self.description})
    for test_case in self.test_cases:
        case_elem = ET.SubElement(campaign, 'testcase', attrib={'id': str(test_case.case_id), 'description': test_case.description, 'result': str(test_case.result)})
        for step in test_case.steps:
            step_elem = ET.SubElement(case_elem, 'teststep', attrib={'id': str(step.step_id), 'message': step.message, 'result': step.result})
    return ET.tostring(campaign, encoding='unicode')


def campaign_to_html(self, test_campaign_name):
    html = f"<html><body><h1>Test Campaign {self.campaign_id}</h1><p>{self.description}</p>"
    for test_case in self.test_cases:
        html += f"<h2>Test Case {test_case.case_id}</h2><p>{test_case.description}</p><table border='1'><tr><th>Step ID</th><th>Message</th><th>Result</th></tr>"
        for step in test_case.steps:
            html += f"<tr><td>{step.step_id}</td><td>{step.message}</td><td>{step.result}</td></tr>"
        html += f"</table><p>Overall Result: {test_case.result}</p>"
    html += "</body></html>"
    return html


