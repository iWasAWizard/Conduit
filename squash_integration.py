import requests

class ConduitSquashTMIntegration:
    def __init__(self, base_url, auth_token):
        self.base_url = base_url
        self.auth_token = auth_token
        self.headers = {'Authorization': f'Bearer {self.auth_token}', 'Content-Type': 'application/json'}

    def post_test_result(self, project_id, test_result):
        url = f"{self.base_url}/projects/{project_id}/results"
        response = requests.post(url, headers=self.headers, json=test_result)
        return response.status_code, response.json()
