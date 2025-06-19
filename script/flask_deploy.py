"""
Note:
    This file provides a local Flask web server for triggering ETL (Extract, Transform, Load) tasks via an HTTP GET endpoint.

    - Exposes the `/etl` route for local development and testing.
    - Accepts `start_row_index`, `end_row_index`, and `source` as query parameters to control the ETL job.
    - Uses `main_task.main` for processing and `write_log` for status logging.
    - Returns plain text logs on success, or JSON error responses on failure.
    - Intended for local use only. For cloud deployment, see the Azure Functions version.

    To run locally:
        $ python local_deploy.py
        # Then visit: http://127.0.0.1:8181/etl?start_row_index=1&end_row_index=100&source=training
"""

from flask import Flask, request, jsonify, Response

from batch_cleaning import main
from util_task_logger import write_log

app = Flask(__name__)

@app.route("/etl", methods=["GET"])
def etl():
    # Get parameters from query string
    start_row_index = request.args.get('start_row_index')
    end_row_index = request.args.get('end_row_index')
    source = request.args.get('source')

    write_log(start_row_index, end_row_index, source, status='started')
    result = main(start_row_index, end_row_index, source)
    log = write_log(
        start_row_index,
        end_row_index,
        source,
        result.get('status', 'failed'),
        message=result.get('message', None)
    )

    # You can decide what you want to return as a response
    if start_row_index and end_row_index:
        if result:
            return Response(log, mimetype="text/plain")
        else:
            return jsonify({"error": "Processing failed", "details": result}), 400
    else:
        return (
            "This endpoint executed successfully. "
            "Pass a start_row_index and end_row_index in the query string for a personalized response.",
            200
        )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8181, debug=True)