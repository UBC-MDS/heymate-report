# This script orchestrates the batch ETL process for menu data.
# It fetches raw data from SQL Server, cleans it using an LLM-based extractor, and uploads the results.
# To use it, call `main(start_row_index, end_row_index, source)`
# Supported sources: "training" or "testing" → determines which table to read from and write to.

from sql_reader import get_data_batch
from sql_uploader import process_and_upload
from llm_menu_extractor import run_qc_extraction
from write_log import write_log

def main(start_row_index: int, end_row_index: int, source: str):
    """
    Runs a batch ETL process for menu data from a given source.

    Parameters
    ----------
    start_row_index : int
        The starting index (inclusive) of rows to fetch from the database.
    end_row_index : int
        The ending index (inclusive) of rows to fetch.
    source : str
        The data source to read from, should be either 'training' or 'testing'.

    Returns
    -------
    dict
        A dictionary with ETL status and number of processed records, or error message if failed.
    """
    try:
        df = get_data_batch(start_row_index, end_row_index, source)
        cleaned_results = run_qc_extraction(df)
        process_and_upload(cleaned_results, source=source)
        return {
            "status": "success",
            "processed": len(cleaned_results)
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

if __name__ == "__main__":
    # Example arguments
    start_row_index = 1
    end_row_index = 3
    source = "training"

    result = main(start_row_index, end_row_index, source)
    print(result)