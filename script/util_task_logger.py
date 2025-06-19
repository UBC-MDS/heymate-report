# This script logs ETL batch processing status to the SQL Server table `Log_mds`.
# It captures row range, source, status, optional message, and a UTC timestamp.
# To use it, call `write_log(start_row_index, end_row_index, source, status, message=None)`
# Example status values include: 'started', 'success', or 'error'.

from util_database_reader import connect_to_sql_server
from util_database_uploader import create_table_if_not_exists
from datetime import datetime, timezone

def write_log(start_row_index, end_row_index, source, status, message=None):
    """
    Write a log entry to the Log_mds table in SQL Server.

    Parameters
    ----------
    start_row_index : int
        The starting index of the processed data batch.
    end_row_index : int
        The ending index of the processed data batch.
    source : str
        The name or tag of the data source being processed (e.g., 'training').
    status : str
        Status of the ETL operation (e.g., 'started', 'completed', 'failed').
    message : str, optional
        Optional descriptive message or error information for the log.

    Returns
    -------
    None
    """
    table_name = "Log_mds"
    conn, cursor = connect_to_sql_server()

    # Define schema
    schema_sql = f"""
    CREATE TABLE {table_name} (
        start_row INT,
        end_row INT,
        source NVARCHAR(50),
        status NVARCHAR(20),
        message NVARCHAR(1000),
        log_time DATETIME
    )
    """

    try:
        create_table_if_not_exists(cursor, conn, table_name, schema_sql)
        timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(
            f"""
            INSERT INTO {table_name} (start_row, end_row, source, status, message, log_time)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (start_row_index, end_row_index, source, status, message, timestamp)
        )
        conn.commit()
        print(f"Log written: {status} ({start_row_index}-{end_row_index})")
    except Exception as e:
        print(f"Failed to write log: {e}")
        conn.rollback()
    finally:
        conn.close()
