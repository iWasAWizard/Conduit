squash_integration = ConduitSquashTMIntegration(base_url="http://api.squashtm.example.com", auth_token="your_token_here")
test_result = {
    "test_id": "12345",
    "status": "passed",
    "details": "Test completed successfully."
}
status_code, response = squash_integration.post_test_result(project_id="67890", test_result=test_result)
print("Status Code:", status_code)
print("Response:", response)
