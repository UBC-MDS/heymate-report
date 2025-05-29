from flask import Flask, request, jsonify, Response

from main_task import main
from write_log import write_log

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