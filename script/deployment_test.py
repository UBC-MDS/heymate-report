"""
Note:
    This script tests both OpenAI API token validity and database connection.

    - Verifies that the OpenAI API token is working by sending a test prompt.
    - Writes the result to the log to confirm both API and DB connectivity.
    - Use this script as a basic deployment check before running production workloads.
"""

from write_log import write_log
from llm_menu_extractor import OpenAIConnector
MODEL_NAME = "o4-mini"

def test_openai_connector_token_valid():
    connector = OpenAIConnector()
    try:
        output = connector.client.responses.create(
            model="o4-mini",
            input="say hello"
        )
        assert "hello" in output.output_text.lower()
        return 'Open AI Verified'
    except Exception as e:
        return 'Open AI Verification Falied'
    
msg = test_openai_connector_token_valid()
write_log(0, 0, 'deployment_testing', status='success', message=msg)