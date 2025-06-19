"""
Note:
    Reminder: Azure deployment has currently been paused due to technical challenges.
    
    This file defines an Azure Functions HTTP-triggered endpoint for ETL operations.

    - Exposes an HTTP route (`/etl`) that accepts `start_row_index`, `end_row_index`, and `source` as query parameters.
    - Logs the start and completion status of each ETL job for monitoring and debugging.
    - Calls the main ETL processing logic in `main_task.main`, and logs results using `write_log`.
    - Designed to be deployed as part of an Azure Functions app with anonymous authentication.

    Example usage (HTTP GET):
        /api/etl?start_row_index=1&end_row_index=100&source=training
"""

import azure.functions as func
import logging

from script.batch_cleaning import main
from script.util_task_logger import write_log
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="etl")
def etl(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    start_row_index, end_row_index, source = req.params.get('start_row_index'), req.params.get('end_row_index'), req.params.get('source'),
    write_log(start_row_index, end_row_index, source, status='started')
    result = main(start_row_index, end_row_index, source)
    log = write_log(start_row_index, end_row_index, source, result.get('status', 'failed'), message=result.get('message', None))
    
    if start_row_index and end_row_index:
        if result:
            # Write
            return func.HttpResponse(log)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a start_row_index and end_row_index in the query string or in the request body for a personalized response.",
             status_code=200
        )
