from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
db_path = Path(__file__).resolve().parent / 'employee_events.db'


# OPTION 1: MIXIN
# Define a class called `QueryMixin`
class QueryMixin:
    """
    Mixin class to execute SQL queries and return results.

    Attributes:
        db_path (str): Path to the employee_events database file.

    Methods:
        pandas_query(sql_query: str)
            Executes the SQL query and returns the result as a DataFrame.

        query(sql_query: str)
            Executes the SQL query and returns the result as a list of tuples.
    """
    # Define a method named `pandas_query`
    # that receives an sql query as a string
    # and returns the query's result
    # as a pandas dataframe

    def pandas_query(self, sql_query: str):
        """
        Execute a SQL query to return a pandas DataFrame

        Args:
            sql_query (str): A SQL query string

        Returns:
            A pandas DataFrame of the query results
        """
        conn = connect(db_path)
        df = pd.read_sql_query(sql_query, conn)
        conn.close()
        return df

    # Define a method named `query`
    # that receives an sql_query as a string
    # and returns the query's result as
    # a list of tuples. (You will need
    # to use an sqlite3 cursor)

    def query(self, sql_query: str):
        """
        Execute a SQL query to return a list of tuples

        Args:
            sql_query (str): A SQL query string

        Returns:
            A list of tuples of the query results
        """
        conn = connect(db_path)
        cursor = conn.cursor()
        tuple_list = cursor.execute(sql_query).fetchall()
        cursor.close()
        conn.close()
        return tuple_list


# Leave this code unchanged
def query2(func):
    """
    Decorator that runs a standard sql execution
    and returns a list of tuples
    """

    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result

    return run_query
