import azure.functions as func
from script.main_task import main  # Calls your existing logic

def main(req: func.HttpRequest) -> func.HttpResponse:
    result = main(1, 3, "testing")  # Sample inputs
    return func.HttpResponse(str(result), status_code=200)
